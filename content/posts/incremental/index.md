+++
title = 'Modernizing incrementally'
date = 2026-07-10
draft = false
description = ""
author = "Cesar Romero"
authorLink = "https://www.linkedin.com/in/romerocesar/"
linkedinURL = ""
toc = false
lightgallery = false
linkToMarkdown = false
+++

A client recently asked whether they should modernize their monolithic web application incrementally or rewrite it from scratch to make it work better with AI agents.

I think that framing is too limiting because it ties the destination to the journey.

The destination is usually clear: a modern backend API, a modern frontend that consumes it, and an MCP server that exposes the same capabilities to AI agents without going through a UI designed for humans.

The important insight is that these pieces don't have to arrive together.

As soon as the first API endpoint is available, value starts compounding. The existing UI can call the new API, the MCP server can expose that functionality to agents, and a new frontend can begin migrating one screen at a time.

This approach also reduces risk. Each component is deployed, tested, and validated independently instead of replacing multiple major systems at once and trying to debug all of them after a single release.

For many organizations, the real choice isn't incremental vs. rewrite. It's whether you can define a target architecture that lets both paths converge on the same destination. The answer is probably yes
