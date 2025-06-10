import React from 'react';
import Layout from '@theme/Layout';
import Hero from '@site/src/components/Hero';
import Link from '@docusaurus/Link';

export default function Home(): React.ReactElement {
  return (
    <Layout
      title="Composable scientific micro-models"
      description="Turn any scientific formula into a live API in minutes."
    >
      <Hero
        title={<>Turn any scientific formula<br/>into a live API in minutes.</>}
        subtitle="MCP-Sim is a toolkit for scientists and engineers to deploy, compose, and scale complex models with zero friction."
      >
        <Link
          className="button button--primary button--lg"
          to="/docs"
        >
          Get Started
        </Link>
      </Hero>
    </Layout>
  );
}