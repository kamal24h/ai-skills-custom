---
name: woocommerce
description: Expert WooCommerce development covering products, orders, cart, checkout, payments, shipping, emails, REST API, and admin. Extends WordPress agent with WooCommerce-specific hooks, data models, and patterns. Triggers on "WooCommerce", "WC_", "woocommerce_", "product", "order", "cart", "checkout", "payment gateway", "shipping method".
model: inherit
---

# WooCommerce Development

WooCommerce-specific development patterns extending WordPress best practices. Covers backend conventions, products, orders, checkout, and performance.

**This skill extends the `wordpress` skill.** All WordPress standards and security patterns apply.

## Specialized Agents

Specialized personas for WooCommerce development. Load these from `agents/` to provide expert context.

| Agent | Role | Focus |
|-------|------|-------|
| **woocommerce-pro** | WC Expert | Products, orders, cart/checkout, payments, shipping, REST API. |

## When to Use

Reference these guidelines when:
- Building WooCommerce extensions, plugins, or themes
- Customizing products, orders, cart, or checkout flows
- Creating custom payment gateways or shipping methods
- Extending the WooCommerce REST API
- Optimizing store performance and database queries
- Handling order status transitions and fulfillment logic

## Step 1: Detect WooCommerce Environment

**Always check WooCommerce version and active features before giving advice.**

```bash
# Check WC version
wp eval "echo WC_VERSION;"
# Check for specific features (e.g. HPOS)
wp option get woocommerce_custom_orders_table_enabled
```

> **Version baseline:** this skill's hook reference is extracted from WooCommerce **11.x** source. Hook signatures and availability may differ on older versions — verify against the detected `WC_VERSION`.

## Core Directives

### MUST DO

- Use **CRUD classes** (`WC_Product`, `WC_Order`, etc.) instead of direct metadata access
- Follow WooCommerce naming conventions and hook priority standards
- Ensure **Data Integrity** by verifying entities before modification
- Implement proper logging via `WC_Logger`
- Support **HPOS (High-Performance Order Storage)** in all new code
- Use `WC_Query` for custom product/order lookups
- Redact sensitive data from checkout and email templates

### MUST NOT DO

- Access WooCommerce metadata directly via `get_post_meta` (use getters/setters)
- Modify core WooCommerce tables directly
- Hardcode currency symbols or price formats
- Perform expensive calculations inside the cart or checkout loop without caching
- Use deprecated hooks (e.g., `woocommerce_add_to_cart_redirect`)
- Overwrite template files if a hook-based solution is possible

## Category Index — When to Load Which Reference

| # | Category | Impact | Rule file | Load when… |
|--:|----------|:------:|-----------|------------|
| 1 | Backend Conventions | CRITICAL | [`rules/woo-backend-dev.md`](rules/woo-backend-dev.md) | Class structure, DI, naming conventions |
| 2 | Data Integrity | CRITICAL | [`rules/woo-data-integrity.md`](rules/woo-data-integrity.md) | Verifying entities before modification, CRUD safety |
| 3 | Hook Conventions | CRITICAL | [`rules/woo-hooks-conventions.md`](rules/woo-hooks-conventions.md) | Callback naming, priorities, removing hooks |
| 4 | Products | CRITICAL | [`rules/woo-product-development.md`](rules/woo-product-development.md) | Product types, inventory, pricing |
| 5 | Orders | CRITICAL | [`rules/woo-order-processing.md`](rules/woo-order-processing.md) | Statuses, fulfillment, refunds |
| 6 | Payments | CRITICAL | [`rules/woo-payment-gateways.md`](rules/woo-payment-gateways.md) | Gateway development, webhooks |
| 7 | Checkout | HIGH | [`rules/woo-checkout.md`](rules/woo-checkout.md) | Fields, validation, order creation |
| 8 | Emails | MEDIUM | [`rules/woo-email-customization.md`](rules/woo-email-customization.md) | Email triggers, templates, headers |
| 9 | Shipping | HIGH | [`rules/woo-shipping.md`](rules/woo-shipping.md) | Custom shipping methods, rates |
| 10 | REST API | HIGH | [`rules/woo-rest-api.md`](rules/woo-rest-api.md) | Extending or consuming the WC REST API |
| 11 | Admin | LOW | [`rules/woo-admin.md`](rules/woo-admin.md) | Admin screens, settings pages, notices |
| 12 | Performance | HIGH | [`rules/woo-performance.md`](rules/woo-performance.md) | Cache priming, query optimization |

All rules live in `rules/` — one file per category, each with Bad/Good examples and a closing `Reference:` link.

## Hook Discovery Protocol

`references/hooks/` documents **2,621 unique core hooks** (11 action + 11 filter files), extracted from the WooCommerce 11.x plugin source: typed `**Params:**` where docblocks exist, raw `**Args:**` at call sites otherwise, plus `**Since:**` version and description where documented.

**DO NOT** read hook files blindly. Use this protocol:

1.  **Exact Search:** `grep_search(pattern='^### woocommerce_add_to_cart$', include_pattern='references/hooks/*.md')`
2.  **Keyword Discovery:** `grep_search(pattern='order_status', include_pattern='references/hooks/*.md')`
3.  **Variable Hooks:** Check `references/variable-hooks.md` for patterns like `woocommerce_order_status_{$status}`.

## Validation Checklist

- [ ] All data access uses WooCommerce CRUD methods (getters/setters)
- [ ] HPOS compatibility is verified
- [ ] Custom fields are properly sanitized and escaped
- [ ] No N+1 queries in product loops or order lists
- [ ] Payment and shipping methods follow the official base classes
- [ ] Email templates are customized via hooks, not just overrides
- [ ] Currency and price formatting uses native WC functions
- [ ] Order status transitions are handled via the appropriate hooks

## External References

- [WooCommerce Developer Documentation](https://developer.woocommerce.com)
- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce REST API Documentation](https://woocommerce.github.io/woocommerce-rest-api-docs/)
- [HPOS Development Guide](https://github.com/woocommerce/woocommerce/wiki/High-Performance-Order-Storage-Upgrade-Guide)
