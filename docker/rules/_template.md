# Rule Template

## Use When

- Describe the Docker task or failure mode that should load this rule.

## Prefer

- State the preferred Docker or Compose pattern.

## Avoid

- State the anti-pattern and why it creates operational risk.

## Verify

```bash
docker compose config
docker build .
```
