---
name: docker
description: Unified Docker and Docker Compose skill covering Dockerfiles, BuildKit, multi-stage builds, Compose services/resources, image/container CLI, architecture, networking, storage, security, CI/CD, production hardening, Go templates, generation, review, and troubleshooting. Use when building, reviewing, auditing, debugging, optimizing, or containerizing applications with Docker, Docker Compose, Docker Engine, BuildKit, registries, images, containers, volumes, or networks.
---

# Docker (Unified)

A single, comprehensive skill for Docker Engine, BuildKit, Dockerfiles, Docker Compose v2, image/container workflows, production readiness, security hardening, and troubleshooting.

> **Version baseline:** targets Docker Engine **29.x** (current stable; 28.x reached end of support in May 2026) and Compose v2. Verify the host version with `docker version` before relying on newest features.
>
> **Related skills:** containerizing Go services → `golang` · PHP/Laravel apps → `php`/`laravel` · Node/TS services → `javascript` · service deployment patterns (health probes, graceful shutdown) → `microservices`.

## Specialized Agents

Specialized personas for Docker work. Load these from `agents/` to provide expert context.

| Agent | Role | Focus |
|-------|------|-------|
| **docker-pro** | Docker Expert | Generate, review, harden, optimize, and debug Dockerfiles, Compose stacks, images, containers, storage, networking, and CI/CD. |

## When to Use

Apply this skill when working on Docker or Compose for any of the following:
- Creating or improving Dockerfiles, `.dockerignore`, entrypoints, or image builds
- Designing multi-stage builds, BuildKit cache/secret/SSH mounts, or buildx workflows
- Writing or validating `compose.yaml`, services, networks, volumes, configs, secrets, and profiles
- Running, inspecting, logging, pruning, tagging, saving, loading, or publishing images and containers
- Hardening containers with non-root users, capabilities, read-only filesystems, seccomp/AppArmor, scanning, or resource limits
- Persisting data with named volumes, bind mounts, tmpfs, backups, and cleanup
- Debugging build, runtime, Compose, or networking failures
- Preparing production containers, health checks, restart policies, logging, and CI/CD registry workflows

## Step 1: Detect Docker Environment

Always identify the local Docker and Compose setup before changing advice into commands:

```bash
docker version
docker compose version
docker info
docker context ls
```

When a project has existing Docker files, inspect them first:

```bash
docker compose config
docker image ls
docker container ls --all
```

## Core Directives

### MUST DO

- Use `# syntax=docker/dockerfile:1` for Dockerfiles that rely on BuildKit features.
- Prefer multi-stage builds; keep compilers, package managers, and SDKs out of runtime images.
- Copy dependency manifests before source code to preserve layer cache.
- Add a `.dockerignore` for every build context.
- Use specific image tags; require digest pinning for high-reproducibility production paths.
- Run application containers as non-root unless the workload has a documented kernel-level reason.
- Use exec form for `ENTRYPOINT` and `CMD`; entrypoint scripts must finish with `exec "$@"`.
- Add meaningful health checks for long-running services.
- Use named volumes for persistent data and `tmpfs` for disposable sensitive or scratch data.
- Bind development ports to `127.0.0.1` when host-wide exposure is not needed.
- Validate Compose with `docker compose config` before running or reviewing behavior.
- Scan production images with Docker Scout, Trivy, or the repository's established scanner.

### MUST NOT DO

- Do not use `latest` for production image tags.
- Do not bake secrets into `ARG`, `ENV`, image layers, Compose environment values, or committed `.env` files.
- Do not use `ADD` when `COPY` is sufficient.
- Do not rely on anonymous volumes for database persistence.
- Do not use `container_name` on scalable Compose services.
- Do not use `privileged: true`, host networking, mounted Docker sockets, or broad capabilities without explicit justification.
- Do not assume `depends_on` means the dependency is ready; use health checks and `condition: service_healthy`.
- Do not run containers without CPU/memory limits in production.
- Do not write application logs only to files inside containers; use stdout/stderr and host log rotation.

## Category Index - When to Load Which Reference

| # | Category | Impact | Load when... | Reference | Rules |
|--:|----------|:------:|--------------|-----------|:------|
| 1 | Dockerfile Syntax | CRITICAL | Writing Dockerfiles, choosing instructions, CMD vs ENTRYPOINT, COPY vs ADD, health checks | [`references/syntax-dockerfile.md`](references/syntax-dockerfile.md) | `dockerfile-` |
| 2 | BuildKit | CRITICAL | Using cache mounts, secrets, SSH mounts, bind/tmpfs mounts, heredocs, cache backends | [`references/syntax-buildkit.md`](references/syntax-buildkit.md) | `buildkit-`, `build-` |
| 3 | Multi-Stage Builds | CRITICAL | Reducing image size, separating build/runtime dependencies, creating target stages | [`references/syntax-multistage.md`](references/syntax-multistage.md) | `dockerfile-`, `build-`, `production-` |
| 4 | Compose Services | CRITICAL | Defining services, ports, env, healthchecks, depends_on, logging, profiles, deploy | [`references/syntax-compose-services.md`](references/syntax-compose-services.md) | `compose-` |
| 5 | Compose Resources | HIGH | Defining networks, volumes, configs, secrets, IPAM, aliases, external resources | [`references/syntax-compose-resources.md`](references/syntax-compose-resources.md) | `compose-`, `storage-`, `networking-` |
| 6 | Production | CRITICAL | Preparing production images/stacks, base images, signals, labels, health, minimal attack surface | [`references/impl-production.md`](references/impl-production.md) | `production-`, `security-` |
| 7 | Security | CRITICAL | Hardening, vulnerability scans, non-root, capabilities, read-only rootfs, seccomp/AppArmor | [`references/core-security.md`](references/core-security.md) | `security-` |
| 8 | Build Optimization | HIGH | Improving build time, cache invalidation, `.dockerignore`, package caches, CI cache reuse | [`references/impl-build-optimization.md`](references/impl-build-optimization.md) | `build-` |
| 9 | Networking | HIGH | Bridge/host/overlay/macvlan/ipvlan, DNS, service discovery, port publishing, connectivity | [`references/core-networking.md`](references/core-networking.md) | `networking-` |
| 10 | Storage | HIGH | Volumes, bind mounts, tmpfs, database persistence, backup/restore, cleanup | [`references/impl-storage.md`](references/impl-storage.md) | `storage-` |
| 11 | CI/CD | HIGH | GitHub Actions, buildx, QEMU, Docker Hub/GHCR auth, multi-platform image publishing | [`references/impl-cicd.md`](references/impl-cicd.md) | `cicd-`, `build-` |
| 12 | Compose Workflows | MEDIUM | Overrides, profiles, includes, `compose.override.yaml`, env precedence, compose watch | [`references/impl-compose-workflows.md`](references/impl-compose-workflows.md) | `compose-` |
| 13 | Container CLI | MEDIUM | Running, execing, logging, inspecting, stats, events, lifecycle, cp/diff/ps | [`references/syntax-cli-containers.md`](references/syntax-cli-containers.md) | `cli-`, `runtime-` |
| 14 | Image CLI | MEDIUM | Build/buildx, pull, push, tag, prune, save/load, history, manifest, system cleanup | [`references/syntax-cli-images.md`](references/syntax-cli-images.md) | `cli-`, `build-` |
| 15 | Go Templates | MEDIUM | Formatting Docker command output with `--format`, inspect scripts, custom tables | [`references/impl-go-templates.md`](references/impl-go-templates.md) | `cli-` |
| 16 | Architecture | MEDIUM | Explaining Docker Engine, daemon, containerd, runc, OCI, layers, lifecycle, build context | [`references/core-architecture.md`](references/core-architecture.md) | `architecture-` |
| 17 | Build Errors | HIGH | Debugging build context, COPY/ADD, cache, BuildKit mount, platform, ARG/ENV errors | [`references/errors-build.md`](references/errors-build.md) | `errors-`, `build-` |
| 18 | Runtime Errors | HIGH | Debugging crashes, OOM, permissions, ports, exec format, read-only filesystem, PID limits | [`references/errors-runtime.md`](references/errors-runtime.md) | `errors-`, `runtime-` |
| 19 | Compose Errors | HIGH | Debugging `docker compose up`, dependency timeouts, interpolation, profiles, config validation | [`references/errors-compose.md`](references/errors-compose.md) | `errors-`, `compose-` |
| 20 | Networking Errors | HIGH | Debugging DNS, connection refused, port publishing, internet access, subnet/firewall conflicts | [`references/errors-networking.md`](references/errors-networking.md) | `errors-`, `networking-` |

## Agent Reference Index

The combined `docker-pro` agent uses these generation and review references when producing or auditing Docker assets:

- [`references/agent-generator-templates.md`](references/agent-generator-templates.md)
- [`references/agent-generator-compose-templates.md`](references/agent-generator-compose-templates.md)
- [`references/agent-generator-anti-patterns.md`](references/agent-generator-anti-patterns.md)
- [`references/agent-review-checklist.md`](references/agent-review-checklist.md)
- [`references/agent-review-examples.md`](references/agent-review-examples.md)
- [`references/agent-review-anti-patterns.md`](references/agent-review-anti-patterns.md)

## Rule Index

Refer to the specific prefixes in `rules/` for concrete review and implementation guardrails:
- `architecture-`, `dockerfile-`, `buildkit-`, `build-`, `compose-`, `production-`, `security-`, `networking-`, `storage-`, `cicd-`, `cli-`, `runtime-`, `errors-`.

## Validation Checklist

- [ ] Dockerfile starts with a current syntax directive when BuildKit features are used.
- [ ] Runtime image is minimal and does not include build-only tools.
- [ ] Dependency layers are ordered for cache reuse and build context is trimmed by `.dockerignore`.
- [ ] Containers run as non-root, avoid unnecessary capabilities, and do not contain baked secrets.
- [ ] `ENTRYPOINT`/`CMD` use exec form and signal handling is correct.
- [ ] Services have real health checks and Compose dependencies wait for health when required.
- [ ] Persistent data uses named volumes with backup/restore expectations documented.
- [ ] Production stacks define restart policy, resource limits, log rotation, and scanner workflow.
- [ ] Compose files validate with `docker compose config`.
- [ ] Focused Docker commands or tests have been run, or skipped verification is explicitly reported.

## External References

- [Docker Documentation](https://docs.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/reference/dockerfile/)
- [Compose Specification](https://docs.docker.com/compose/compose-file/)
- [BuildKit](https://docs.docker.com/build/buildkit/)
- [Docker Scout](https://docs.docker.com/scout/)
- [Open Container Initiative](https://opencontainers.org/)
