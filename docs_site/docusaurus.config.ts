import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "MCP-Sim",
  tagline: "Composable scientific micro-models",
  favicon: "img/favicon.ico",

  // ✅ Fix these URLs:
  url: "https://aj-en.github.io",  // Your GitHub Pages domain
  baseUrl: "/mcp-sim/",            // Your repository name

  // ✅ Update these to match your GitHub username:
  organizationName: "AJ-EN",       // Your GitHub username
  projectName: "mcp-sim",          // Your repository name

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  themes: ["@docusaurus/theme-live-codeblock"],
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/AJ-EN/mcp-sim/tree/main/docs/',
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/AJ-EN/mcp-sim/tree/main/docs/',
          authorsMapPath: '../authors.yml',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    navbar: {
      title: "MCP-Sim",
      logo: {
        alt: "MCP-Sim Logo",
        src: "img/logo.svg",
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Documentation",
        },
        { to: "/blog", label: "Changelog", position: "left" },
        {
          href: "https://github.com/AJ-EN/mcp-sim",  // ✅ Updated GitHub link
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [],
      copyright: `Copyright © ${new Date().getFullYear()} MCP-Sim`,
    },
    prism: {
      theme: prismThemes.oneLight,
      darkTheme: prismThemes.oneDark,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;