// commitlint — convention Conventional Commits (décision 023)
// Footer obligatoire : Refs: <ADR-NNNN | DT-NNN | C-NN | Bloc N | Landing Page>
// Trailer DCO obligatoire : Signed-off-by: <Nom> <email>

module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      ['feat', 'fix', 'style', 'feat!', 'fix!', 'docs', 'test', 'refactor', 'chore', 'sec'],
    ],
    'scope-enum': [
      2,
      'always',
      [
        'auth', 'api', 'ui', 'site', 'db', 'ci', 'doc', 'akoris', 'state', 'debt',
        'context', 'audit', 'checklist', 'license', 'readme', 'changelog',
        'decisions', 'scripts', 'bootstrap', 'contributing', 'method',
      ],
    ],
    'subject-case': [0],
    'footer-max-line-length': [2, 'always', 200],
    'trailer-exists': [2, 'always', 'Signed-off-by:'],
  },
};
