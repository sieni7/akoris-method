// commitlint — convention Conventional Commits (décision 023)
// Footer obligatoire : Refs: <ADR-NNNN | DT-NNN | C-NN | Bloc N>

module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      ['feat', 'fix', 'feat!', 'fix!', 'docs', 'test', 'refactor', 'chore', 'sec'],
    ],
    'scope-enum': [
      2,
      'always',
      [
        'auth', 'api', 'ui', 'db', 'ci', 'doc', 'akoris', 'state', 'debt',
        'context', 'audit', 'checklist', 'license', 'readme', 'changelog',
        'decisions', 'scripts', 'bootstrap',
      ],
    ],
    'subject-case': [0],
    'footer-max-line-length': [2, 'always', 200],
  },
};
