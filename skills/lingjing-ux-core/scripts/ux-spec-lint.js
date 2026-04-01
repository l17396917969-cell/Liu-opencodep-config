#!/usr/bin/env node
/**
 * ux-spec-lint.js — 灵境UX规范 ux_spec 类名校验器 v1.0.0
 *
 * 用途：AI 产出 ux_spec YAML 后，在写入 .yml 前执行此脚本校验
 *       所有 component_roles[*].lingjing_core_class 类名是否合规。
 *
 * 用法：
 *   node scripts/ux-spec-lint.js <ux_spec.yml文件路径>
 *   node scripts/ux-spec-lint.js examples/ux_spec_supply_chain.yml
 *
 * 选项：
 *   --registry <path>   指定 class_registry.json 路径（默认：../lingjing-ui-core/data/class_registry.json）
 *   --fix               自动将 alias 类名归一化为 canonical（输出到同文件或 --out）
 *   --out <path>        与 --fix 配合，指定修复后输出路径（默认覆盖原文件）
 *
 * 退出码：
 *   0 = PASS（无 ERROR）
 *   1 = FAIL（有 ERROR 项）
 */

const fs = require('fs');
const path = require('path');

// ── CLI 参数 ──────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
if (args.length === 0 || args.includes('--help')) {
  console.log('Usage: node scripts/ux-spec-lint.js <ux_spec.yml> [--registry <path>] [--fix] [--out <path>]');
  process.exit(0);
}

const specPath = args[0];
const registryIdx = args.indexOf('--registry');
const fixMode = args.includes('--fix');
const outIdx = args.indexOf('--out');

const DEFAULT_REGISTRY = path.resolve(__dirname, '../../lingjing-ui-core/data/class_registry.json');
const registryPath = registryIdx >= 0 && args[registryIdx + 1]
  ? path.resolve(args[registryIdx + 1])
  : DEFAULT_REGISTRY;

const outPath = outIdx >= 0 && args[outIdx + 1]
  ? path.resolve(args[outIdx + 1])
  : (fixMode ? path.resolve(specPath) : null);

// ── 文件加载 ──────────────────────────────────────────────────────────────
if (!fs.existsSync(specPath)) {
  console.error('[ERROR] ux_spec file not found:', specPath);
  process.exit(1);
}
if (!fs.existsSync(registryPath)) {
  console.error('[ERROR] class_registry.json not found:', registryPath);
  console.error('  → Run: node ../lingjing-ui-core/scripts/build-registry.js');
  process.exit(1);
}

const specContent = fs.readFileSync(specPath, 'utf8');
const registry = JSON.parse(fs.readFileSync(registryPath, 'utf8')).classes;

// ── 提取 lingjing_core_class 值 ──────────────────────────────────────────
function extractCoreClasses(yamlContent) {
  const results = [];
  const lines = yamlContent.split('\n');
  lines.forEach((line, idx) => {
    const m = line.match(/lingjing_core_class\s*:\s*["']?([a-zA-Z][a-zA-Z0-9_-]+)["']?/);
    if (m) {
      results.push({ class: m[1], lineNum: idx + 1, raw: line.trim() });
    }
  });
  return results;
}

// ── 校验单个类名 ──────────────────────────────────────────────────────────
function checkClass(cls) {
  const entry = registry[cls];
  if (!entry) {
    return { status: 'ERROR', reason: 'not_in_registry', message: `"${cls}" 不在 class_registry.json 中，可能是拼写错误或未收录的类名` };
  }
  switch (entry.type) {
    case 'canonical':
      return { status: 'PASS', reason: 'canonical', scenes: entry.scenes };
    case 'utility':
      return { status: 'PASS', reason: 'utility', scenes: entry.scenes };
    case 'demo_only':
      return { status: 'ERROR', reason: 'demo_only', message: `"${cls}" 是 demo_only 类，禁止在业务 ux_spec 中引用；请改用业务语义组件类` };
    case 'deprecated':
      return { status: 'WARN', reason: 'deprecated', message: `"${cls}" 已废弃，建议改用: ${entry.use_instead}`, use_instead: entry.use_instead };
    case 'alias':
      return { status: 'WARN', reason: 'alias', message: `"${cls}" 是别名，应归一化为: "${entry.canonical}"`, canonical: entry.canonical };
    default:
      return { status: 'WARN', reason: 'unknown_type', message: `"${cls}" 类型未知: ${entry.type}` };
  }
}

// ── 执行校验 ──────────────────────────────────────────────────────────────
const found = extractCoreClasses(specContent);
const results = found.map(item => ({
  ...item,
  ...checkClass(item.class)
}));

const errors  = results.filter(r => r.status === 'ERROR');
const warns   = results.filter(r => r.status === 'WARN');
const passes  = results.filter(r => r.status === 'PASS');

// ── --fix 模式：自动归一化 alias ──────────────────────────────────────────
let fixedContent = specContent;
if (fixMode) {
  const aliases = results.filter(r => r.reason === 'alias');
  if (aliases.length > 0) {
    aliases.forEach(item => {
      // Replace the class name in the YAML content
      const pattern = new RegExp(
        `(lingjing_core_class\\s*:\\s*["']?)${item.class}(["']?)`,
        'g'
      );
      fixedContent = fixedContent.replace(pattern, `$1${item.canonical}$2`);
    });
    fs.writeFileSync(outPath, fixedContent);
    console.log(`\n[FIX] ${aliases.length} alias(es) normalized → ${outPath}`);
  } else {
    console.log('\n[FIX] No aliases found to normalize.');
  }
}

// ── 报告输出 ──────────────────────────────────────────────────────────────
const RED    = '\x1b[31m';
const GREEN  = '\x1b[32m';
const YELLOW = '\x1b[33m';
const CYAN   = '\x1b[36m';
const BOLD   = '\x1b[1m';
const RESET  = '\x1b[0m';

console.log('\n' + BOLD + '── ux-spec-lint.js v1.0.0 ──' + RESET);
console.log(CYAN + 'File:     ' + RESET + specPath);
console.log(CYAN + 'Registry: ' + RESET + registryPath);
console.log(CYAN + 'Classes found: ' + RESET + found.length);
console.log('');

if (errors.length > 0) {
  console.log(RED + BOLD + `[ERROR] ${errors.length} class(es) failed:` + RESET);
  errors.forEach(r => {
    console.log(`  Line ${r.lineNum}: ${RED}${r.class}${RESET}`);
    console.log(`    → ${r.message}`);
  });
  console.log('');
}

if (warns.length > 0) {
  console.log(YELLOW + BOLD + `[WARN] ${warns.length} class(es) need attention:` + RESET);
  warns.forEach(r => {
    const fix = r.canonical
      ? ` (建议改为: ${r.canonical})`
      : r.use_instead ? ` (建议改为: ${r.use_instead})` : '';
    console.log(`  Line ${r.lineNum}: ${YELLOW}${r.class}${RESET}${fix}`);
  });
  console.log('');
}

if (passes.length > 0 && errors.length === 0 && warns.length === 0) {
  console.log(GREEN + BOLD + `✓ PASS — 全部 ${passes.length} 个类名校验通过` + RESET);
} else if (errors.length === 0) {
  console.log(YELLOW + BOLD + `⚠ WARN — 无 ERROR，${warns.length} 项需处理（${passes.length} 项通过）` + RESET);
  if (!fixMode && warns.filter(w => w.reason === 'alias').length > 0) {
    console.log(YELLOW + '  提示：运行 --fix 可自动归一化 alias 类名' + RESET);
  }
} else {
  console.log(RED + BOLD + `✗ FAIL — ${errors.length} ERROR, ${warns.length} WARN, ${passes.length} PASS` + RESET);
  console.log(RED + '  请修复 ERROR 项后重新落盘 ux_spec' + RESET);
}

// ── 写 JSON 报告 ──────────────────────────────────────────────────────────
const reportPath = path.join(path.dirname(path.resolve(specPath)), 'ux-spec-lint-report.json');
const report = {
  _meta: { linter: 'ux-spec-lint.js v1.0.0', ui_skill_version: '3.1.6' },
  file: specPath,
  timestamp: new Date().toISOString(),
  pass: errors.length === 0,
  summary: {
    total_classes: found.length,
    pass: passes.length,
    warn: warns.length,
    error: errors.length,
  },
  errors: errors.map(r => ({ line: r.lineNum, class: r.class, reason: r.reason, message: r.message })),
  warnings: warns.map(r => ({ line: r.lineNum, class: r.class, reason: r.reason, message: r.message, fix: r.canonical || r.use_instead })),
  delivery_gate: errors.length === 0
    ? 'PASS — ux_spec 类名校验通过，可继续 UI 落地'
    : 'FAIL — 存在 ERROR 项，禁止将此 ux_spec 传递给 UI 落地环节，必须先修复',
};
fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
console.log('\nReport: ' + reportPath);
console.log('');

process.exit(errors.length > 0 ? 1 : 0);
