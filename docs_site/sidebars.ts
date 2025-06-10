import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    { type: 'doc', id: 'intro', label: 'Introduction' },
    { type: 'doc', id: 'quick-start', label: 'Quick Start' },
    {
      type: 'category',
      label: 'Core Concepts',
      collapsible: false,
      items: [
        'sdk-overview',
        'schema-spec',
      ],
    },
    {
      type: 'category',
      label: 'Guides',
      collapsible: true,
      items: [
        'local-testing',
        'docker-deploy',
      ],
    },
    {
      type: 'category',
      label: 'Reference',
      collapsible: true,
      items: [
        'cli-reference',
        'router-api',
      ],
    },
    'contributing',
    'faq',
  ],
};

export default sidebars;