# WooCommerce Actions: REST API

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### rest_api_init
**Args:** $wp_rest_server
**Tags:** #action

### rest_delete_product_review
**Params:** object $product_review, WP_REST_Response $response, WP_REST_Request $request
**Tags:** #action
Fires after a product review is deleted via the REST API.

### woocommerce_api_$API_REQUEST
**Tags:** #action

### woocommerce_api_request
**Args:** $api_request
**Tags:** #action

### woocommerce_api_wc_gateway_paypal
**Tags:** #action

### woocommerce_rest_api_uploaded_image_from_url
**Args:** $file, $image_url
**Tags:** #action

### woocommerce_rest_delete_$TAXONOMY
**Tags:** #action

### woocommerce_rest_delete_$THIS->POST_TYPE
**Tags:** #action

### woocommerce_rest_delete_$THIS->POST_TYPE_object
**Tags:** #action

### woocommerce_rest_delete_customer
**Params:** WP_User $user_data, WP_REST_Response $response, WP_REST_Request $request
**Tags:** #action
Fires after a customer is deleted via the REST API.

### woocommerce_rest_delete_order_note
**Params:** WP_Comment $note, WP_REST_Response $response, WP_REST_Request $request
**Tags:** #action
Fires after a order note is deleted or trashed via the REST API.

### woocommerce_rest_delete_product_attribute
**Params:** stdObject $attribute, WP_REST_Response $response, WP_REST_Request $request
**Tags:** #action
Fires after a single attribute is deleted via the REST API.

### woocommerce_rest_delete_review
**Params:** WP_Comment $review, WP_REST_Response $response, WP_REST_Request $request
**Tags:** #action
Fires after a review is deleted via the REST API.

### woocommerce_rest_delete_shipping_zone_method
**Params:** WC_Shipping_Method $method, WC_Shipping_Zone $zone, WP_REST_Response $response, WP_REST_Request $request
**Since:** 9.1.0 | **Tags:** #action
Fires after a shipping zone is deleted via the REST API.

### woocommerce_rest_delete_tax
**Params:** stdClass $tax_class, WP_REST_Response $response, WP_REST_Request $request
**Tags:** #action
Fires after a tax class is deleted via the REST API.

### woocommerce_rest_delete_webhook_object
**Params:** WC_Webhook $webhook, WP_REST_Response $response, WP_REST_Request $request
**Tags:** #action
Fires after a single item is deleted or trashed via the REST API.

### woocommerce_rest_insert_$TAXONOMY
**Tags:** #action

### woocommerce_rest_insert_$THIS->POST_TYPE
**Tags:** #action

### woocommerce_rest_insert_$THIS->POST_TYPE_object
**Tags:** #action

### woocommerce_rest_insert_customer
**Params:** WP_User $user_data, WP_REST_Request $request, boolean $creating
**Tags:** #action
Fires after a customer is created or updated via the REST API.

### woocommerce_rest_insert_order_note
**Params:** WP_Comment $note, WP_REST_Request $request, boolean $creating
**Tags:** #action
Fires after a order note is created or updated via the REST API.

### woocommerce_rest_insert_product
**Params:** WP_Post $post, WP_REST_Request $request, boolean $creating
**Tags:** #action
Fires after a single item is created or updated via the REST API.

### woocommerce_rest_insert_product_attribute
**Params:** stdObject $attribute, WP_REST_Request $request, boolean $creating
**Tags:** #action
Fires after a single product attribute is created or updated via the REST API.

### woocommerce_rest_insert_product_review
**Params:** WP_Comment $review, WP_REST_Request $request, bool $creating
**Tags:** #action
Fires after a comment is created or updated via the REST API.

### woocommerce_rest_insert_system_status_tool
**Params:** array $tool, WP_REST_Request $request
**Tags:** #action
Fires after a WooCommerce REST system status tool has been executed.

### woocommerce_rest_insert_tax
**Params:** stdClass $tax, WP_REST_Request $request, boolean $creating
**Tags:** #action
Fires after a tax is created or updated via the REST API.

### woocommerce_rest_insert_tax_class
**Params:** stdClass $tax_class, WP_REST_Request $request, boolean $creating
**Tags:** #action
Fires after a tax class is created or updated via the REST API.

### woocommerce_rest_insert_webhook_object
**Params:** WC_Webhook $webhook, WP_REST_Request $request, bool $creating
**Tags:** #action
Fires after a single item is created or updated via the REST API.

### woocommerce_rest_order_actions_email_send
**Params:** int $order_id, string $template_id
**Since:** 9.8.0 | **Tags:** #action
Action to trigger sending a custom order email template from a REST API request. The email template must first be made available for the associated order. See the `woocommerce_rest_order_actions_email_valid_template_classes` filter hook.

### woocommerce_rest_remove_order_item
**Params:** WC_Order_Item $item
**Since:** 9.3.0. | **Tags:** #action
Allow extensions be notified before the item is removed.

### woocommerce_rest_save_product_variation
**Args:** $variation->get_id(), $menu_order, $data
**Tags:** #action

### woocommerce_rest_set_order_item
**Params:** WC_Order_Item $item, array $posted
**Since:** 4.5.0. | **Tags:** #action
Allow extensions be notified before the item is saved.

### woocommerce_restock_refunded_item
**Args:** $product->get_id(), $old_stock, $new_stock, $order, $product
**Tags:** #action

### woocommerce_restore_cart_item
**Args:** $cart_item_key, $this
**Tags:** #action

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
