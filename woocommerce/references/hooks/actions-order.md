# WooCommerce Actions: Order

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_after_order_notes
**Args:** $checkout
**Tags:** #action

### woocommerce_before_order_notes
**Args:** $checkout
**Tags:** #action

### woocommerce_order_details_after_customer_details
**Args:** $order
**Tags:** #action

### woocommerce_order_details_after_order_table
**Args:** $order
**Tags:** #action

### woocommerce_order_details_after_order_table_items
**Args:** $order
**Tags:** #action

### woocommerce_order_details_before_order_table
**Args:** $order
**Tags:** #action

### woocommerce_order_details_before_order_table_items
**Args:** $order
**Tags:** #action

### woocommerce_order_item_meta_end
**Params:** int $item_id, WC_Order_Item_Product $item, WC_Order $order, bool $plain_text
**Since:** 2.3.0 | **Tags:** #action
Allow other plugins to add additional product information.

### woocommerce_order_item_meta_start
**Params:** int $item_id, WC_Order_Item_Product $item, WC_Order $order, bool $plain_text
**Since:** 2.3.0 | **Tags:** #action
Allow other plugins to add additional product information.

### woocommerce_order_tracking_form
**Tags:** #action

### woocommerce_order_tracking_form_end
**Tags:** #action

### woocommerce_order_tracking_form_start
**Tags:** #action

### woocommerce_pay_order_after_submit
**Tags:** #action

### woocommerce_pay_order_before_payment
**Tags:** #action

### woocommerce_pay_order_before_submit
**Tags:** #action

### woocommerce_receipt_$ORDER->GET_PAYMENT_METHOD
**Tags:** #action

### woocommerce_review_order_after_order_total
**Tags:** #action

### woocommerce_review_order_after_payment
**Tags:** #action

### woocommerce_review_order_after_submit
**Tags:** #action

### woocommerce_review_order_before_order_total
**Tags:** #action

### woocommerce_review_order_before_payment
**Tags:** #action

### woocommerce_review_order_before_submit
**Tags:** #action

### woocommerce_view_order
**Args:** $order_id
**Tags:** #action

### woocommerce_track_order
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_before_delete_order_item
**Args:** $item->get_id()
**Tags:** #action

### woocommerce_delete_order
**Params:** int $order_id
**Since:** 2.7.0 | **Tags:** #action
Fires immediately after an order is deleted.

### woocommerce_delete_order_item
**Args:** $item->get_id()
**Tags:** #action

### woocommerce_delete_order_refund
**Params:** int $id
**Since:** 3.0.0 | **Tags:** #action
Fires when a refund is deleted.

### woocommerce_new_order
**Args:** $order->get_id(), $order
**Since:** 2.7.0 | **Tags:** #action
Fires when a new order is created.

### woocommerce_new_order_item
**Args:** $item->get_id(), $item, $item->get_order_id()
**Tags:** #action

### woocommerce_order_object_updated_props
**Params:** WC_Abstract_Order $order, string[] $updated_props
**Since:** 2.7.0 | **Tags:** #action
Action fired after updating order properties.

### woocommerce_order_refund_object_updated_props
**Args:** $refund, $updated_props
**Since:** 2.7.0 | **Tags:** #action
Fires after updating meta for a order refund.

### woocommerce_trash_order
**Params:** int $order_id
**Since:** 2.7.0 | **Tags:** #action
Fires immediately after an order is trashed.

### woocommerce_update_order
**Args:** $order->get_id(), $order
**Tags:** #action

### woocommerce_update_order_item
**Args:** $item->get_id(), $item, $item->get_order_id()
**Tags:** #action

### woocommerce_update_order_refund
**Params:** int $refund_id, \WC_Order_Refund $refund
**Since:** 10.4.0 | **Tags:** #action
Fires when an order refund is updated.

### order_edit_form_tag
**Params:** \WC_Order $order
**Since:** 6.9.0 | **Tags:** #action
Fires inside the order edit form tag.

### order_edit_form_top
**Params:** \WC_Order $order
**Since:** 8.0.0 | **Tags:** #action
Fires at the top of the order edit form. Can be used as a replacement for edit_form_top hook for HPOS.

### wc_marketplace_suggestions_orders_empty_state
**Tags:** #action

### woocommerce_after_order_fee_item_name
**Args:** $item_id, $item, null
**Tags:** #action

### woocommerce_after_order_itemmeta
**Args:** $item_id, $item, $product
**Tags:** #action

### woocommerce_after_order_refund_item_name
**Args:** $refund
**Tags:** #action

### woocommerce_after_resend_order_email
**Args:** $order, 'customer_invoice'
**Since:** 1.0.0 | **Tags:** #action
Fires after an order email has been resent.

### woocommerce_ajax_add_order_item_meta
**Args:** $item_id, $item, $order
**Tags:** #action

### woocommerce_ajax_order_items_added
**Args:** $added_items, $order
**Tags:** #action

### woocommerce_ajax_order_items_removed
**Params:** int $item_id, WC_Order_Item|false $item, bool|array|WP_Error $changed_store, bool|WC_Order|WC_Order_Refund $order
**Since:** 5.2.0 | **Tags:** #action
Fires after order items are removed.

### woocommerce_analytics_delete_order_stats
**Params:** int $order_id, int $customer_id
**Since:** 4.0.0 | **Tags:** #action
Fires when orders stats are deleted.

### woocommerce_analytics_update_order_stats
**Params:** int $order_id
**Since:** 4.0.0. | **Tags:** #action
Fires when order's stats reports are updated.

### woocommerce_before_order_item_$ITEM->GET_TYPE_html
**Tags:** #action

### woocommerce_before_order_itemmeta
**Args:** $item_id, $item, $product
**Tags:** #action

### woocommerce_before_resend_order_emails
**Args:** $order, 'customer_invoice'
**Since:** 1.0.0 | **Tags:** #action
Fires before an order email is resent.

### woocommerce_before_save_order_item
**Args:** $item
**Tags:** #action

### woocommerce_before_save_order_items
**Params:** int $order_id, array $items
**Since:** 2.2 | **Tags:** #action
Save order items. Uses the CRUD.

### woocommerce_cancelled_order
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_create_refund
**Args:** $refund, $args
**Tags:** #action

### woocommerce_delete_order_downloadable_permissions
**Params:** int $postid
**Tags:** #action
Remove downloadable permissions on permanent order deletion.

### woocommerce_delete_order_items
**Args:** $postid
**Tags:** #action

### woocommerce_delete_shop_order_transients
**Args:** $order_id
**Tags:** #action

### woocommerce_deleted_order_downloadable_permissions
**Args:** $postid
**Tags:** #action

### woocommerce_deleted_order_items
**Args:** $postid
**Tags:** #action

### woocommerce_order_action_sanitize_title$ACTION
**Tags:** #action

### woocommerce_order_actions_end
**Args:** $order_id
**Since:** 2.1.0 | **Tags:** #action
Fires at the end of order actions meta box rendering.

### woocommerce_order_actions_start
**Args:** $order_id
**Since:** 2.1.0 | **Tags:** #action
Fires at the start of order actions meta box rendering.

### woocommerce_order_after_calculate_totals
**Args:** $and_taxes, $this
**Tags:** #action

### woocommerce_order_applied_coupon
**Params:** WC_Coupon $coupon, WC_Order $order
**Since:** 7.3 | **Tags:** #action
Action to signal that a coupon has been applied to an order.

### woocommerce_order_before_calculate_taxes
**Params:** array $args
**Tags:** #action
Calculate taxes for all line items and shipping, and store the totals and tax rows. If by default the taxes are based on the shipping address and the current order doesn't have any, it would use the billing address rather than using the Shopping base location. Will use the base country unless customer addresses are set.

### woocommerce_order_before_calculate_totals
**Params:** bool $and_taxes
**Since:** 2.2 | **Tags:** #action
Calculate totals by looking at the contents of the order. Stores the totals and returns the orders final total.

### woocommerce_order_edit_product
**Args:** $this->get_id(), $item->get_id(), $args, $product
**Tags:** #action

### woocommerce_order_edit_status
**Args:** $id, $new_status
**Tags:** #action

### woocommerce_order_fully_refunded
**Args:** $order->get_id(), $refund->get_id()
**Tags:** #action

### woocommerce_order_fully_refunded_notification
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_order_item_$ITEM->GET_TYPE_html
**Tags:** #action

### woocommerce_order_item_add_action_buttons
**Args:** $order
**Tags:** #action

### woocommerce_order_item_add_line_buttons
**Args:** $order
**Tags:** #action

### woocommerce_order_item_after_calculate_taxes
**Args:** $this, $calculate_tax_for
**Tags:** #action

### woocommerce_order_item_fee_after_calculate_taxes
**Args:** $this, $calculate_tax_for
**Tags:** #action

### woocommerce_order_item_shipping_after_calculate_taxes
**Args:** $this, $calculate_tax_for
**Tags:** #action

### woocommerce_order_list_table_extra_tablenav
**Params:** string $order_type, string $which
**Since:** 7.3.0 | **Tags:** #action
Fires immediately following the closing "actions" div in the tablenav for the order list table.

### woocommerce_order_list_table_restrict_manage_orders
**Params:** string $order_type, string $which
**Since:** 7.3.0 | **Tags:** #action
Fires before the "Filter" button on the list table for orders and other order types.

### woocommerce_order_note_added
**Params:** int $order_note_id, WC_Order $order
**Since:** 4.4.0 | **Tags:** #action
Action hook fired after an order note is added.

### woocommerce_order_note_deleted
**Params:** int $note_id, stdClass $note
**Since:** 9.1.0 | **Tags:** #action
Action hook fired after an order note is deleted.

### woocommerce_order_partially_refunded
**Args:** $order->get_id(), $refund->get_id()
**Tags:** #action

### woocommerce_order_partially_refunded_notification
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_order_payment_status_changed
**Args:** $this->get_id(), $this
**Since:** 3.9.0 | **Tags:** #action
Fires when the order progresses from a pending payment status to a paid one.

### woocommerce_order_refunded
**Args:** $order->get_id(), $refund->get_id()
**Tags:** #action

### woocommerce_order_save_attribution_data
**Params:** WC_Order $order, array $params
**Since:** 8.5.0 | **Tags:** #action
Run an action to save order attribution data.

### woocommerce_order_scheduler_after_import_order
**Params:** int $order_id
**Since:** 10.3.0 | **Tags:** #action
Fires after an order or refund has been imported into Analytics lookup tables and the reports cache has been invalidated.

### woocommerce_order_status_$STATUS_TRANSITION[from]_to_$STATUS_TRANSITION[to]
**Tags:** #action

### woocommerce_order_status_$STATUS_TRANSITION[to]
**Tags:** #action

### woocommerce_order_status_changed
**Args:** $this->get_id(), $status_transition['from'], $status_transition['to'], $this
**Tags:** #action

### woocommerce_order_status_completed_notification
**Args:** $order->get_id(), $order
**Tags:** #action

### woocommerce_order_status_failed_notification
**Args:** $order->get_id(), $order
**Tags:** #action

### woocommerce_order_status_pending_to_on-hold_notification
**Args:** $order->get_id(), $order
**Tags:** #action

### woocommerce_order_status_pending_to_processing_notification
**Args:** $order->get_id(), $order
**Tags:** #action

### woocommerce_order_update_coupon
**Args:** $this->get_id(), $item->get_id(), $args
**Tags:** #action

### woocommerce_order_update_fee
**Args:** $this->get_id(), $item->get_id(), $args
**Tags:** #action

### woocommerce_order_update_shipping
**Args:** $this->get_id(), $item->get_id(), $args
**Tags:** #action

### woocommerce_order_update_tax
**Args:** $this->get_id(), $item->get_id(), $args
**Tags:** #action

### woocommerce_payment_complete
**Args:** $this->get_id(), $transaction_id
**Tags:** #action

### woocommerce_payment_complete_order_status_$THIS->GET_STATUS
**Tags:** #action

### woocommerce_payment_token_added_to_order
**Args:** $this->get_id(), $token->get_id(), $token, $token_ids
**Tags:** #action

### woocommerce_paypal_standard_order_created_response
**Params:** int|string $http_code, array $response_data, WC_Order $order
**Since:** 10.4.0 | **Tags:** #action
Fires after receiving a response from PayPal order creation. This hook allows extensions to react to PayPal API responses, such as displaying admin notices or logging response data. Note: This hook fires on EVERY order creation attempt (success or failure), and can be called multiple times for the same order if retried. Extensions hooking this should be idempotent and check order state/meta before taking action to avoid duplicate processing.

### woocommerce_pre_payment_complete
**Args:** $this->get_id(), $transaction_id
**Tags:** #action

### woocommerce_privacy_before_remove_order_personal_data
**Params:** WC_Order $order
**Since:** 3.4.0 | **Tags:** #action
Allow extensions to remove their own personal data for this order first, so order data is still available.

### woocommerce_privacy_remove_order_personal_data
**Params:** WC_Order $order
**Since:** 3.4.0 | **Tags:** #action
Allow extensions to remove their own personal data for this order.

### woocommerce_process_shop_order_meta
**Params:** int $post_id, object $post
**Since:** 2.1.0 | **Tags:** #action
Save meta for shop order.

### woocommerce_reduce_order_item_stock
**Params:** WC_Order_Item_Product $item, array $change, WC_Order $order
**Since:** 7.6.0 | **Tags:** #action
Fires when stock reduced to a specific line item

### woocommerce_reduce_order_stock
**Args:** $order
**Tags:** #action

### woocommerce_refund_created
**Args:** $refund->get_id(), $args
**Tags:** #action

### woocommerce_refund_deleted
**Args:** $refund_id, $order_id
**Tags:** #action

### woocommerce_remove_order_items
**Params:** WC_Order $this, string|null $type
**Since:** 7.8.0 | **Tags:** #action
Trigger action before removing all order line items. Allows you to track order items.

### woocommerce_remove_order_personal_data
**Args:** $order
**Tags:** #action

### woocommerce_removed_order_items
**Params:** WC_Order $this, string|null $type
**Since:** 7.8.0 | **Tags:** #action
Trigger action after removing all order line items from the database.

### woocommerce_restore_order_item_stock
**Params:** WC_Order_Item_Product $item, int $new_stock, int $old_stock, WC_Order $order
**Since:** 9.1.0 | **Tags:** #action
Fires when stock restored to a specific line item

### woocommerce_restore_order_stock
**Args:** $order
**Tags:** #action

### woocommerce_resume_order
**Params:** int $order_id
**Since:** 3.0.0 | **Tags:** #action
Indicates that we are resuming checkout for an existing order (which is pending payment, and which has not changed since it was added to the current shopping session).

### woocommerce_saved_order_items
**Args:** $order_id, $items
**Tags:** #action

### woocommerce_store_api_cart_update_order_from_request
**Params:** \WC_Order $draft_order, \WC_Customer $customer, \WP_REST_Request $request
**Since:** 7.2.0 | **Tags:** #action
Fires when the order is synced with cart data from a cart route.

### woocommerce_store_api_checkout_update_order_meta
**Params:** \WC_Order $order
**Since:** 7.2.0 | **Tags:** #action
Fires when the Checkout Block/Store API updates an order's meta data. This hook gives extensions the chance to add or update meta data on the $order. Throwing an exception from a callback attached to this action will make the Checkout Block render in a warning state, effectively preventing checkout. This is similar to existing core hook woocommerce_checkout_update_order_meta. We're using a new action: - To keep the interface focused (only pass $order, not passing request data). - This also explicitly indicates these orders are from checkout block/StoreAPI.

### woocommerce_untrash_order
**Params:** int $order_id, string $previous_status
**Since:** 7.2.0 | **Tags:** #action
Fires before an order is restored from the trash.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
