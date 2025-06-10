import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "MCP-Sim",
  tagline: "Composable scientific micro-models",
  favicon: "img/favicon.ico",

  // --- CONFIGURATIONS FOR GITHUB PAGES DEPLOYMENT ---
  url: "https://AJ-EN.github.io", // ✅ This is correct
  baseUrl: "/mcp-sim-starter-kit/", // ✅ CORRECTED: Must match the repo name
  organizationName: "AJ-EN", // ✅ This is correct
  projectName: "mcp-sim-starter-kit", // ✅ CORRECTED: Must match the repo name

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  themes: ["@docusaurus/theme-live-codeblock"],
  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",
          // ✅ CORRECTED: Points to the new public repo
          editUrl: "https://github.com/AJ-EN/mcp-sim-starter-kit/tree/main/",
        },
        blog: {
          showReadingTime: true,
          // ✅ CORRECTED: Points to the new public repo
          editUrl: "https://github.com/AJ-EN/mcp-sim-starter-kit/tree/main/",
          // ✅ REMOVED: authorsMapPath was pointing to a deleted file
        },
        theme: {
          customCss: "./src/css/custom.css",
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
          // ✅ CORRECTED: Points to the new public repo
          href: "https://github.com/AJ-EN/mcp-sim-starter-kit",
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
