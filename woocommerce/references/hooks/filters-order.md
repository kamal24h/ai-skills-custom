# WooCommerce Filters: Order

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_order_button_html
**Args:** '<button type="submit" class="button alt' . esc_attr( wc_wp_theme_get_element_class_name( 'button' ) ? ' ' . wc_wp_theme_get_element_class_name( 'button' ) : '' ) . '" name="woocommerce_checkout_place_order" id="place_order" value="' . esc_attr( $order_button_text ) . '" data-value="' . esc_attr( $order_button_text ) . '">' . esc_html( $order_button_text ) . '</button>'
**Tags:** #filter

### woocommerce_order_details_status
**Params:** string $order_status
**Since:** 10.1.0 | **Tags:** #filter
Filter to modify order detiails status text.

### woocommerce_order_item_class
**Params:** string $class, WC_Order_Item_Product $item, WC_Order $order
**Since:** 2.1.0 | **Tags:** #filter
Email Order Item Class hook.

### woocommerce_order_item_name
**Params:** string $item_name, WC_Order_Item $item, bool $is_visible
**Since:** 9.9.0 | **Tags:** #filter
Filter the order item name.

### woocommerce_order_item_permalink
**Args:** $is_visible ? $product->get_permalink( $item ) : '', $item, $order
**Tags:** #filter

### woocommerce_order_item_quantity_html
**Args:** '<strong class="product-quantity">' . sprintf( '&times;&nbsp;%s', $qty_display ) . '</strong>', $item
**Tags:** #filter

### woocommerce_order_item_thumbnail
**Params:** string $image, WC_Order_Item_Product $item
**Since:** 2.1.0 | **Tags:** #filter
Email Order Item Thumbnail hook.

### woocommerce_order_item_visible
**Params:** bool $visible, WC_Order_Item_Product $item
**Since:** 2.1.0 | **Tags:** #filter
Email Order Item Visibility hook. This filter allows you to control the visibility of order items in emails.

### woocommerce_order_tracking_status
**Params:** string $order_status
**Since:** 10.1.0 | **Tags:** #filter
Filter to modify order tracking status text.

### woocommerce_pay_order_button_html
**Args:** '<button type="submit" class="button alt' . esc_attr( wc_wp_theme_get_element_class_name( 'button' ) ? ' ' . wc_wp_theme_get_element_class_name( 'button' ) : '' ) . '" id="place_order" value="' . esc_attr( $order_button_text ) . '" data-value="' . esc_attr( $order_button_text ) . '">' . esc_html( $order_button_text ) . '</button>'
**Tags:** #filter

### woocommerce_purchase_note_order_statuses
**Params:** \WC_Order $order, \WC_Product|false $product
**Tags:** #filter
Render an item purchase note.

### woocommerce_purchase_order_item_types
**Args:** OrderItemType::LINE_ITEM
**Tags:** #filter

### woocommerce_thankyou_order_received_text
**Params:** string $message, WC_Order|false $order
**Since:** 2.2.0 | **Tags:** #filter
Filter the message shown after a checkout is complete.

### woocommerce_order_button_text
**Args:** __( 'Place order', 'woocommerce' )
**Tags:** #filter

### woocommerce_order_downloads_table_show_downloads
**Args:** ( $order->has_downloadable_item() && $order->is_download_permitted() ), $order
**Tags:** #filter

### woocommerce_valid_order_statuses_for_order_again
**Params:** array $valid_statuses
**Since:** 3.6.0 | **Tags:** #filter
Filter the valid order statuses for reordering.

### woocommerce_order_received_verify_known_shoppers
**Params:** bool $verify_known_shoppers
**Since:** 8.4.0 | **Tags:** #filter
Indicates if known (non-guest) shoppers need to be logged in before we let them access the order received page.

### woocommerce_pay_order_button_text
**Params:** string $text
**Since:** 3.0.2 | **Tags:** #filter
Allows the text of the submit button on the Pay for Order page to be changed.

### woocommerce_thankyou_order_id
**Args:** absint( $wp->query_vars['order-received'] )
**Tags:** #filter

### woocommerce_thankyou_order_key
**Args:** empty( $_GET['key'] ) ? '' : wc_clean( wp_unslash( $_GET['key'] ) )
**Tags:** #filter

### woocommerce_default_order_status
**Params:** string $status
**Since:** 3.0.0 | **Tags:** #filter
In view context, return the default status if no status has been set.

### woocommerce_load_order_cogs_value
**Params:** float $cogs_value, WC_Abstract_Order $order
**Since:** 9.5.0 | **Tags:** #filter
Filter to customize the Cost of Goods Sold value that gets loaded for a given order.

### woocommerce_load_order_item_cogs_value
**Params:** float $cogs_value, WC_Order_Item $product
**Since:** 9.5.0 | **Tags:** #filter
Filter to customize the Cost of Goods Sold value that gets loaded for a given order item.

### woocommerce_new_order_data
**Params:** array $data
**Since:** 3.3.0 | **Tags:** #filter
Filters the data for a new order before it is inserted into the database.

### woocommerce_order_data_store_cpt_get_orders_query
**Args:** $wp_query_args, $query_vars, $this
**Tags:** #filter

### woocommerce_order_data_store_cpt_query_unsupported_args
**Params:** array $unsupported_args
**Since:** 9.2.0 | **Tags:** #filter
Allows 3rd parties to filter query args that will trigger an unsupported notice.

### woocommerce_payment_complete_order_status
**Params:** string $status, int $order_id, WC_Order $this
**Since:** 2.7.0 | **Tags:** #filter
Filters the order status to set after payment complete.

### woocommerce_save_order_cogs_value
**Params:** float|null $cogs_value, WC_Abstract_Order $item
**Since:** 9.5.0 | **Tags:** #filter
Filter to customize the Cost of Goods Sold value that gets saved for a given order, or to suppress the saving of the value (so that custom storage can be used).

### woocommerce_save_order_item_cogs_value
**Params:** float|null $cogs_value, WC_Order_Item $item
**Since:** 9.5.0 | **Tags:** #filter
Filter to customize the Cost of Goods Sold value that gets saved for a given order item, or to suppress the saving of the value (so that custom storage can be used).

### woocommerce_shop_order_search_fields
**Args:** array(
					'_billing_address_index',
					'_shipping_address_index',
					'_billing_last_name',
					'_billing_email',
					'_billing_phone',
				)
**Tags:** #filter

### woocommerce_shop_order_search_results
**Params:** array $order_ids, string $term, array $search_fields
**Since:** 3.0.0 | **Tags:** #filter
Filter the order ids to be returned.

### wc_allow_changing_orders_storage_while_sync_is_pending
**Params:** bool $allow
**Since:** 8.3.0 | **Tags:** #filter
Filter to allow changing where order data is stored, even when there are orders pending synchronization. DANGER! This filter is intended for usage when doing manual and automated testing in development environments only, it should NEVER be used in production environments. Order data corruption or loss can happen!

### wc_order_attribution_allow_multiple_elements
**Params:** bool $allow_multiple_elements
**Since:** 10.5.0 | **Tags:** #filter
Filter to allow sites to opt back into single-output behavior.

### wc_order_attribution_allow_tracking
**Params:** bool $allow_tracking
**Since:** 8.5.0 | **Tags:** #filter
Filter to allow tracking.

### wc_order_attribution_cookie_lifetime_months
**Params:** float $lifetime
**Since:** 8.5.0 | **Tags:** #filter
Filter the lifetime of the cookie used for source tracking.

### wc_order_attribution_debug_mode_enabled
**Args:** 'no'
**Tags:** #filter

### wc_order_attribution_field_description
**Params:** string $description, string $field_name
**Since:** 8.5.0 | **Tags:** #filter
Filter the description for the order attribution field.

### wc_order_attribution_origin_formatted_source
**Params:** string $formatted_source, string $source
**Since:** 8.5.0 | **Tags:** #filter
Filter the formatted source for the order origin.

### wc_order_attribution_origin_label
**Params:** string $label, string $source_type, string $source, string $formatted_source
**Since:** 8.5.0 | **Tags:** #filter
Filter the label for the order origin. This label should have a %s placeholder for the formatted source to be inserted via sprintf().

### wc_order_attribution_session_length_minutes
**Params:** int $session_length
**Since:** 8.5.0 | **Tags:** #filter
Filter the session length for source tracking.

### wc_order_attribution_stamp_checkout_html_actions
**Params:** array $stamp_checkout_html_actions
**Since:** 9.0.0 | **Tags:** #filter
Filter set of actions used to stamp the checkout order attribution HTML container element.

### wc_order_attribution_tracking_field_prefix
**Params:** string $prefix
**Since:** 8.5.0 | **Tags:** #filter
Filter the prefix for the meta fields.

### wc_order_attribution_tracking_fields
**Params:** string[] $fields
**Since:** 8.5.0 | **Tags:** #filter
Filter the fields to show in the source data metabox.

### wc_order_attribution_use_base64_cookies
**Params:** bool $use_base64_cookies
**Since:** 9.0.0 | **Tags:** #filter
Filter to enable base64 encoding for cookie values.

### wc_order_is_editable
**Params:** bool $is_editable, WC_Order $this
**Since:** 2.7.0 | **Tags:** #filter
Filter to check if an order is editable.

### wc_order_payment_card_info
**Params:** array|null $info, WC_Abstract_Order $order
**Since:** 9.5.0 | **Tags:** #filter
Filter to allow payment gateways to provide payment card info for an order.

### wc_order_statuses
**Args:** $order_statuses
**Tags:** #filter

### wc_order_types
**Args:** $order_types, $for
**Tags:** #filter

### woocommerce_agentic_webhook_order_status_map
**Params:** array $status_map, string $wc_status
**Since:** 10.3.0 | **Tags:** #filter
Filter the WooCommerce to ACP order status mapping. Allows extensions to map custom WooCommerce order statuses to ACP order statuses. The mapped status must be one of: created, manual_review, confirmed, canceled, shipped, fulfilled.

### woocommerce_agentic_webhook_refund_type
**Params:** string $refund_type, WC_Order_Refund $refund
**Since:** 10.4.0 | **Tags:** #filter
Filter the refund type for Agentic webhooks. This allows extensions to specify when a refund is store credit. By default, all refunds are assumed to be original payment method.

### woocommerce_ajax_add_order_item_validation
**Args:** $validation_error, $product, $order, $qty
**Tags:** #filter

### woocommerce_ajax_order_item
**Args:** $order->get_item( $item_id ), $item_id, $order, $product
**Tags:** #filter

### woocommerce_analytics_excluded_order_statuses
**Params:** array $excluded_statuses
**Since:** 4.0.0 | **Tags:** #filter
Filter the list of excluded order statuses for customer history and analytics reports.

### woocommerce_analytics_is_test_order
**Params:** bool $is_test, \WC_Abstract_Order $order
**Since:** 10.7.0 | **Tags:** #filter
Filter whether an order is a test order excluded from analytics. Use this filter to customize test order detection beyond the default WCPay test mode check, e.g., to exclude orders from other payment gateways' test/sandbox modes.

### woocommerce_analytics_orderby_enum_$THIS->REST_BASE
**Tags:** #filter

### woocommerce_analytics_update_order_stats_data
**Params:** array $data, Order|OrderRefund $order
**Since:** 4.0.0 | **Tags:** #filter
Filters order stats data.

### woocommerce_anonymize_completed_orders_query_args
**Args:** array(
					'date_created' => '<' . strtotime( '-' . $option['number'] . ' ' . $option['unit'] ),
					'limit'        => $limit, // Batches of 20.
					'status'       => OrderInternalStatus::COMPLETED,
					'anonymized'   => false,
					'type'         => 'shop_order',
				)
**Tags:** #filter

### woocommerce_anonymize_refunded_orders_query_args
**Params:** string $date_created, int $limit, string $status, string $type
**Since:** 9.8.0 | **Tags:** #filter
Filter to modify the query arguments for anonymizing refunded orders.

### woocommerce_bacs_process_payment_order_status
**Params:** string $default_status, object $order
**Since:** 3.4.0 | **Tags:** #filter
Filter the order status for BACS payment.

### woocommerce_calculated_order_cogs_value
**Params:** float $value, WC_Abstract_Order $order
**Since:** 9.5.0 | **Tags:** #filter
Filter to modify the Cost of Goods Sold value that gets calculated for a given order.

### woocommerce_calculated_order_item_cogs_value
**Params:** float|null $value, WC_Order_Item $line_item
**Since:** 9.5.0 | **Tags:** #filter
Filter to modify the Cost of Goods Sold value that gets calculated for a given order item.

### woocommerce_can_reduce_order_stock
**Args:** true, $order
**Tags:** #filter

### woocommerce_can_restock_refunded_items
**Params:** WC_Order $order, array $refunded_line_items
**Since:** 3.0.0 | **Tags:** #filter
Restock items during refund.

### woocommerce_can_restore_order_stock
**Args:** true, $order
**Tags:** #filter

### woocommerce_cancel_unpaid_order
**Params:** bool $should_cancel, WC_Order $order
**Since:** 2.0.3 | **Tags:** #filter
Filters whether an unpaid order should be automatically cancelled. By default, only orders created via customer-facing checkout (classic checkout or checkout block) are automatically cancelled. Orders created through other means (admin, REST API, plugins) are not cancelled.

### woocommerce_cancel_unpaid_orders_interval_minutes
**Params:** int $cancel_unpaid_interval
**Since:** 5.1.0 | **Tags:** #filter
Filters the interval at which to cancel unpaid orders in minutes.

### woocommerce_cheque_process_payment_order_status
**Params:** string $status, object $order
**Since:** 3.6.0 | **Tags:** #filter
Filter the order status for cheque payment.

### woocommerce_cod_process_payment_order_status
**Params:** string $order_status
**Since:** 2.6.0 | **Tags:** #filter
Filter the order status for COD orders.

### woocommerce_cot_shop_order_search_results
**Args:** $order_ids, $term
**Tags:** #filter

### woocommerce_create_order
**Params:** int|null $order_id, WC_Checkout $checkout
**Since:** 3.0.0 | **Tags:** #filter
Gives plugins an opportunity to create a new order themselves.

### woocommerce_delete_expired_draft_orders_batch_size
**Params:** int $batch_size
**Since:** 10.7.0 | **Tags:** #filter
Filters the number of draft orders deleted per batch during cleanup. Increasing this value can help improve deletion throughput for high-volume or busy stores when the cleanup task cannot keep up with the draft orders backlog.

### woocommerce_empty_cart_when_order_again
**Args:** true
**Tags:** #filter

### woocommerce_filter_fields_for_order_confirmation
**Params:** array $field, array $fields, array $context, CheckoutFields $this
**Since:** 10.1.0 | **Tags:** #filter
Filter fields for order confirmation (thank you page, email). Used in methods: WC_Email::additional_checkout_fields WC_Email::additional_address_fields CheckoutFieldsFrontend::render_order_other_fields AdditionalFields::render_content

### woocommerce_formatted_refund_amount
**Args:** wc_price( $this->get_amount(), array( 'currency' => $this->get_currency() ) ), $this
**Tags:** #filter

### woocommerce_fulfillment_calculate_order_fulfillment_status
**Params:** string $status, WC_Order $order, array $fulfillments
**Since:** 10.1.0 | **Tags:** #filter
This filter allows plugins to modify the fulfillment status of an order.

### woocommerce_fulfillment_created_order_note
**Params:** string|null $message, Fulfillment $fulfillment, \WC_Order $order
**Since:** 10.7.0 | **Tags:** #filter
Filters the order note message when a fulfillment is created. Return null to cancel the note.

### woocommerce_fulfillment_deleted_order_note
**Params:** string|null $message, Fulfillment $fulfillment, \WC_Order $order
**Since:** 10.7.0 | **Tags:** #filter
Filters the order note message when a fulfillment is deleted. Return null to cancel the note.

### woocommerce_fulfillment_order_fulfillment_status_text
**Params:** string $fulfillment_status_text, string $fulfillment_status, WC_Order $order
**Since:** 10.1.0 | **Tags:** #filter
This filter allows plugins to modify the fulfillment status text for an order for their custom fulfillment statuses.

### woocommerce_fulfillment_order_fulfillment_statuses
**Params:** array $order_fulfillment_statuses
**Since:** 10.1.0 | **Tags:** #filter
This filter allows plugins to modify the list of order fulfillment statuses. It can be used to add, remove, or change the order fulfillment statuses available in the WooCommerce Fulfillments system.

### woocommerce_fulfillment_order_status_changed_order_note
**Params:** string|null $message, \WC_Order $order, string $old_status, string $new_status
**Since:** 10.7.0 | **Tags:** #filter
Filters the order note message when the order fulfillment status changes. Return null to cancel the note.

### woocommerce_fulfillment_status_changed_order_note
**Params:** string|null $message, Fulfillment $fulfillment, \WC_Order $order, string $old_status, string $new_status
**Since:** 10.7.0 | **Tags:** #filter
Filters the order note message when a fulfillment status changes. Return null to cancel the note.

### woocommerce_fulfillment_updated_order_note
**Params:** string|null $message, Fulfillment $fulfillment, \WC_Order $order
**Since:** 10.7.0 | **Tags:** #filter
Filters the order note message when a fulfillment is updated. Return null to cancel the note.

### woocommerce_generate_order_key
**Args:** 'order_' . $key
**Tags:** #filter

### woocommerce_get_cancel_order_url
**Params:** string $url, WC_Order $order, string $redirect
**Since:** 2.2.0 | **Tags:** #filter
Filter the URL to cancel the order in the frontend.

### woocommerce_get_cancel_order_url_raw
**Params:** string $url, WC_Order $order, string $redirect
**Since:** 2.2.0 | **Tags:** #filter
Filter the raw URL to cancel the order in the frontend.

### woocommerce_get_edit_order_url
**Args:** $edit_url, $this
**Tags:** #filter

### woocommerce_get_formatted_order_total
**Params:** string $formatted_total, WC_Order $order, string $tax_display, bool $display_refunded
**Tags:** #filter
Filter WooCommerce formatted order total.

### woocommerce_get_item_count_refunded
**Args:** $count, $item_type, $this
**Tags:** #filter

### woocommerce_get_order_address
**Params:** array $address_data, string $address_type
**Since:** 2.4.0 | **Tags:** #filter
Filter: 'woocommerce_get_order_address' Allow developers to change the returned value for an order's billing or shipping address.

### woocommerce_get_order_currency
**Args:** $this->get_currency(), $this
**Tags:** #filter

### woocommerce_get_order_item_classname
**Args:** $classname, $item_type, $id
**Tags:** #filter

### woocommerce_get_order_item_totals
**Args:** $total_rows, $this, $tax_display
**Tags:** #filter

### woocommerce_get_order_item_totals_excl_free_fees
**Args:** empty( $fee['line_total'] ) && empty( $fee['line_tax'] ), $id
**Tags:** #filter

### woocommerce_get_order_note
**Args:** array(
			'id'            => (int) $data->comment_ID,
			'date_created'  => wc_string_to_datetime( $data->comment_date ),
			'content'       => $data->comment_content,
			'customer_note' => (bool) get_comment_meta( $data->comment_ID, 'is_customer_note', true ),
			'added_by'      => __( 'WooCommerce', 'woocommerce' ) === $data->comment_author ? 'system' : $data->comment_author,
			'order_id'      => absint( $data->comment_post_ID ),
		), $data
**Tags:** #filter

### woocommerce_get_order_payment_tokens
**Args:** $tokens, $order_id
**Tags:** #filter

### woocommerce_get_order_status_labels
**Params:** array $action, WC_Order $order
**Since:** 9.1.0 | **Tags:** #filter
Provides an opportunity to modify and extend the order status labels.

### woocommerce_get_view_order_url
**Args:** wc_get_endpoint_url( 'view-order', $this->get_id(), wc_get_page_permalink( 'myaccount' ) ), $this
**Tags:** #filter

### woocommerce_hidden_order_itemmeta
**Params:** string[] $hidden_keys
**Since:** 2.2.0 | **Tags:** #filter
Filters the order item meta keys hidden from the admin order screen.

### woocommerce_hpos_sync_ignored_order_props
**Args:** array()
**Tags:** #filter

### woocommerce_include_processing_order_count_in_menu
**Args:** true
**Tags:** #filter

### woocommerce_is_order_received_page
**Args:** ( $page_id && is_page( $page_id ) && isset( $wp->query_vars['order-received'] ) )
**Tags:** #filter

### woocommerce_menu_order_count
**Args:** wc_processing_order_count()
**Tags:** #filter

### woocommerce_migrate_country_states_for_orders_batch_size
**Params:** int $batch_size, string $country_code, array $old_to_new_states_mapping
**Since:** 7.2.0 | **Tags:** #filter
Filters the value of N, where the maximum count of database records that will be updated in one single run of migrate_country_states_for_orders is N*2*count($old_to_new_states_mapping) if the woocommerce_orders table exists, or N*count($old_to_new_states_mapping) otherwise.

### woocommerce_new_order_email_allows_resend
**Params:** bool $allows
**Since:** 5.0.0 | **Tags:** #filter
Controls if new order emails can be resend multiple times.

### woocommerce_new_order_note_data
**Args:** array(
				'comment_post_ID'      => $this->get_id(),
				'comment_author'       => $comment_author,
				'comment_author_email' => $comment_author_email,
				'comment_author_url'   => '',
				'comment_content'      => $note,
				'comment_agent'        => 'WooCommerce',
				'comment_type'         => 'order_note',
				'comment_parent'       => 0,
				'comment_approved'     => 1,
			), array(
				'order_id'         => $this->get_id(),
				'is_customer_note' => $is_customer_note,
			)
**Tags:** #filter

### woocommerce_order_actions
**Params:** array $actions, WC_Order|null $order
**Since:** 2.1.0 | **Tags:** #filter
Filter: woocommerce_order_actions Allows filtering of the available order actions for an order.

### woocommerce_order_again_cart_item_data
**Args:** array(), $item, $order
**Tags:** #filter

### woocommerce_order_amount_item_subtotal
**Args:** $subtotal, $this, $item, $inc_tax, $round
**Tags:** #filter

### woocommerce_order_amount_item_tax
**Args:** $tax, $item, $round, $this
**Tags:** #filter

### woocommerce_order_amount_item_total
**Args:** $total, $this, $item, $inc_tax, $round
**Tags:** #filter

### woocommerce_order_amount_line_subtotal
**Args:** $subtotal, $this, $item, $inc_tax, $round
**Tags:** #filter

### woocommerce_order_amount_line_tax
**Params:** mixed $item
**Tags:** #filter
Get line tax - useful for gateways.

### woocommerce_order_amount_line_total
**Args:** $total, $this, $item, $inc_tax, $round
**Tags:** #filter

### woocommerce_order_cancelled_notice
**Args:** __( 'Your order was cancelled.', 'woocommerce' )
**Tags:** #filter

### woocommerce_order_cancelled_notice_type
**Args:** 'notice'
**Tags:** #filter

### woocommerce_order_class
**Params:** string $classname, string $order_type, int $order_id
**Since:** 3.0.0 | **Tags:** #filter
Filter classname so that the class can be overridden if extended.

### woocommerce_order_cogs_total_value_html
**Params:** string $total_html, float $total, WC_Order $order
**Since:** 10.3.0 | **Tags:** #filter
Filter to customize the total Cost of Goods Sold (COGS) value HTML for a given order.

### woocommerce_order_discount_to_display
**Args:** wc_price( $this->get_total_discount( TaxDisplayMode::EXCLUSIVE === $tax_display ), array( 'currency' => $this->get_currency() ) ), $this
**Tags:** #filter

### woocommerce_order_email_verification_grace_period
**Params:** int $grace_period, \WC_Order $order, string $context
**Since:** 11.4.0 | **Tags:** #filter
Controls the grace period within which we do not require any sort of email verification step before rendering the 'order received' or 'order pay' pages.

### woocommerce_order_email_verification_required
**Params:** bool $email_verification_required, WC_Order $order, string $context
**Since:** 11.4.0 | **Tags:** #filter
Provides an opportunity to override the (potential) requirement for shoppers to verify their email address before we show information such as the order summary, or order payment page.

### woocommerce_order_formatted_billing_address
**Args:** $this->get_address( 'billing' ), $this
**Tags:** #filter

### woocommerce_order_formatted_line_subtotal
**Args:** $subtotal, $item, $this
**Tags:** #filter

### woocommerce_order_formatted_shipping_address
**Args:** $raw_address, $this
**Tags:** #filter

### woocommerce_order_fully_refunded_status
**Params:** string $parent_status, int $order_id, int $refund_id
**Since:** 2.7.0 | **Tags:** #filter
Filter the status to set the order to when fully refunded.

### woocommerce_order_get_downloadable_items
**Args:** $downloads, $this
**Tags:** #filter

### woocommerce_order_get_formatted_billing_address
**Params:** string $address, array $raw_address, WC_Order $order
**Since:** 3.8.0 | **Tags:** #filter
Filter orders formatted billing address.

### woocommerce_order_get_formatted_shipping_address
**Params:** string $address, array $raw_address, WC_Order $order
**Since:** 3.8.0 | **Tags:** #filter
Filter orders formatted shipping address.

### woocommerce_order_get_items
**Args:** $items, $this, $types
**Tags:** #filter

### woocommerce_order_get_subtotal
**Args:** (float) $subtotal, $this
**Tags:** #filter

### woocommerce_order_get_tax_location
**Args:** $args, $this
**Tags:** #filter

### woocommerce_order_get_tax_totals
**Args:** $tax_totals, $this
**Tags:** #filter

### woocommerce_order_get_total_discount
**Args:** NumberUtil::round( $total_discount, WC_ROUNDING_PRECISION ), $this
**Tags:** #filter

### woocommerce_order_has_status
**Params:** array|string $status
**Tags:** #filter
Checks the order status against a passed in status.

### woocommerce_order_hide_shipping_address
**Params:** array $hide, WC_Order $this
**Since:** 2.7.0 | **Tags:** #filter
Filter to hide the shipping address for an order.

### woocommerce_order_hide_zero_taxes
**Args:** true
**Tags:** #filter

### woocommerce_order_hold_stock_minutes
**Params:** int $minutes, \WC_Order $order
**Since:** 8.8.0 | **Tags:** #filter
Filters the number of minutes an order should reserve stock for. This hook allows the number of minutes that stock in an order should be reserved for to be filtered, useful for third party developers to increase/reduce the number of minutes if the order meets certain criteria, or to exclude an order from stock reservation using a zero value.

### woocommerce_order_is_created_via
**Params:** string $modus
**Since:** 4.0.0 | **Tags:** #filter
Check if order has been created via admin, checkout, or in another way.

### woocommerce_order_is_download_permitted
**Params:** bool $is_download_permitted, WC_Order $this
**Since:** 2.7.0 | **Tags:** #filter
Filter to check if an order is downloadable.

### woocommerce_order_is_paid
**Args:** $this->has_status( wc_get_is_paid_statuses() ), $this
**Tags:** #filter

### woocommerce_order_is_paid_statuses
**Params:** array $statuses
**Since:** 3.0.0 | **Tags:** #filter
Filter the list of statuses which are considered 'paid'.

### woocommerce_order_is_partially_refunded
**Params:** bool $is_partially_refunded, int $order_id, int $refund_id
**Since:** 6.7.0 | **Tags:** #filter
Trigger notification emails. Filter hook to modify the partially-refunded status conditions.

### woocommerce_order_is_pending_statuses
**Params:** array $statuses
**Since:** 3.6.0 | **Tags:** #filter
Filter the list of statuses which are considered 'pending payment'.

### woocommerce_order_is_vat_exempt
**Args:** 'yes' === $this->get_meta( 'is_vat_exempt' ), $this
**Tags:** #filter

### woocommerce_order_item_cogs_html
**Params:** string $html, float $value, WC_Order_Item $product
**Since:** 9.9.0 | **Tags:** #filter
Filter to customize how the Cost of Goods Sold value for an order item gets rendered to HTML.

### woocommerce_order_item_cogs_per_item_tooltip
**Params:** string $tooltip_text, float $cost_per_item, string $formatted_cost_per_item, WC_Order_Item $order_item
**Since:** 9.9.0 | **Tags:** #filter
Filter to customize the text of the "Cost per unit" tooltip for the "Cost" (of Goods Sold) column in the order details page. If an empty string is returned then the tooltip won't be rendered.

### woocommerce_order_item_cogs_refunded_html
**Params:** string $refunded_html, float $refunded_cost, WC_Order_Item $item, WC_Order $order
**Since:** 10.3.0 | **Tags:** #filter
Filter to customize the refunded Cost of Goods Sold (COGS) value HTML for a given order item.

### woocommerce_order_item_display_meta_key
**Args:** $display_key, $meta, $this
**Tags:** #filter

### woocommerce_order_item_display_meta_value
**Args:** $meta_value, $meta, $this->item
**Tags:** #filter

### woocommerce_order_item_get_formatted_meta_data
**Args:** $formatted_meta, $this
**Tags:** #filter

### woocommerce_order_item_legacy_tax_conversion
**Params:** array $converted, float|string $value, WC_Order_Item $item
**Since:** 10.5.0 | **Tags:** #filter
Filter the converted legacy tax value. Allows plugins to customize how legacy scalar tax values are converted to the expected array format.

### woocommerce_order_item_needs_processing
**Params:** bool $needs_processing, \WC_Product $product, int $order_id
**Since:** 2.7.0 | **Tags:** #filter
Filters whether an order line item requires processing. By default, only virtual downloadable items do not require processing; all other items do.

### woocommerce_order_item_no_cogs_html
**Params:** string $html, WC_Order_Item $product
**Since:** 9.9.0 | **Tags:** #filter
Filter to customize how a non-existing Cost of Goods Sold value for an order item (whose has_cogs method returns false) gets rendered to HTML.

### woocommerce_order_item_product
**Params:** WC_Product|false $product, WC_Order_Item_Product $line_item
**Since:** 2.7.0 | **Tags:** #filter
Modifies the product object returned by \WC_Order_Item_Product::get_product.

### woocommerce_order_item_quantity
**Params:** int|float $quantity, WC_Order $order, WC_Order_Item_Product $item
**Tags:** #filter
Filter order item quantity.

### woocommerce_order_items_meta_display
**Args:** $output, $this, $flat
**Tags:** #filter

### woocommerce_order_items_meta_get_formatted
**Args:** $formatted_meta, $this
**Tags:** #filter

### woocommerce_order_list_table_prepare_items_query_args
**Params:** array $query_args
**Since:** 6.9.0 | **Tags:** #filter
Provides an opportunity to modify the query arguments used in the (Custom Order Table-powered) order list table.

### woocommerce_order_needs_payment
**Args:** ( $this->has_status( $valid_order_statuses ) && $this->get_total() > 0 ), $this, $valid_order_statuses
**Tags:** #filter

### woocommerce_order_needs_shipping
**Params:** bool $needs_shipping, WC_Abstract_Order $order
**Since:** 9.9.0 | **Tags:** #filter
Filter to modify the needs shipping value for a given order.

### woocommerce_order_needs_shipping_address
**Args:** $needs_address, $hide, $this
**Tags:** #filter

### woocommerce_order_note_class
**Args:** array_filter( $css_class ), $note
**Tags:** #filter

### woocommerce_order_number
**Args:** $this->get_id(), $this
**Tags:** #filter

### woocommerce_order_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_order_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_order_recalculate_coupons_coupon_object
**Args:** $coupon_object, $coupon_code, $coupon_item, $this
**Tags:** #filter

### woocommerce_order_shipping_to_display
**Args:** $shipping, $this, $tax_display
**Tags:** #filter

### woocommerce_order_shipping_to_display_shipped_via
**Params:** string $tax_display
**Tags:** #filter
Gets shipping (formatted).

### woocommerce_order_shipping_to_display_tax_label
**Params:** string $tax_label, \WC_Order $order, string $tax_display
**Since:** 6.0.0 | **Tags:** #filter
Hook to add tax label to pickup cost.

### woocommerce_order_subtotal_to_display
**Args:** $subtotal, $compound, $this
**Tags:** #filter

### woocommerce_order_table_search_query_meta_keys
**Args:** $meta_fields_to_search
**Tags:** #filter

### woocommerce_order_type_to_group
**Args:** $this->item_types_to_group
**Tags:** #filter

### woocommerce_order_updated_messages
**Args:** array()
**Tags:** #filter

### woocommerce_orders_cot_and_posts_sync_step_size
**Args:** $batch_size
**Tags:** #filter

### woocommerce_orders_table_datastore_db_rows_for_order
**Params:** array $rows, \WC_Order $order, string $context
**Since:** 8.8.0 | **Tags:** #filter
Filters the rows that are going to be inserted or updated during an order save.

### woocommerce_orders_table_datastore_extra_db_rows_for_order
**Args:** array(), $order, $context
**Tags:** #filter

### woocommerce_orders_table_datastore_get_orders_query
**Params:** array $query_vars
**Since:** 10.4.0 | **Tags:** #filter
Filter the query args before executing the query.

### woocommerce_orders_table_datastore_should_save_after_meta_change
**Params:** bool $should_save
**Since:** 8.8.0 | **Tags:** #filter
Allows code to skip a full order save() when metadata is changed.

### woocommerce_payment_complete_reduce_order_stock
**Args:** ! $stock_reduced, $order_id
**Tags:** #filter

### woocommerce_paypal_force_one_line_item
**Args:** false, $order
**Tags:** #filter

### woocommerce_paypal_get_order_item_name
**Args:** $item_name, $order, $item
**Tags:** #filter

### woocommerce_paypal_get_order_item_names
**Args:** implode( ', ', $item_names ), $order
**Tags:** #filter

### woocommerce_paypal_line_item
**Args:** array(
				'item_name'   => html_entity_decode( wc_trim_string( $item_name ? wp_strip_all_tags( $item_name ) : __( 'Item', 'woocommerce' ), 127 ), ENT_NOQUOTES, 'UTF-8' ),
				'quantity'    => (int) $quantity,
				'amount'      => wc_float_to_string( (float) $amount ),
				'item_number' => $item_number,
			), $item_name, $quantity, $amount, $item_number
**Tags:** #filter

### woocommerce_paypal_refund_request
**Args:** $request, $order, $amount, $reason
**Tags:** #filter

### woocommerce_paypal_use_orders_v2
**Params:** bool $use_orders_v2
**Since:** 10.2.0 | **Tags:** #filter
Filters whether the gateway should use Orders v2 API.

### woocommerce_printable_order_receipt_css
**Args:** $css, $order
**Tags:** #filter

### woocommerce_printable_order_receipt_data
**Params:** array $data, WC_Abstract_Order $order
**Since:** 9.0.0 | **Tags:** #filter
Filter to customize the set of data that is used to render the receipt. The formatted line items aren't included, use the woocommerce_printable_order_receipt_formatted_line_item filter to customize those. See the value returned by the 'get_order_data' and 'get_woo_pay_data' methods for a reference of the structure of the data. See the template file, Templates/order-receipt.php, for reference on how the data is used.

### woocommerce_printable_order_receipt_line_item_display_data
**Params:** string $line_item_display_data, array $line_item_data, WC_Abstract_Order $order
**Since:** 9.0.0 | **Tags:** #filter
Filter to customize the HTML that gets rendered for each order line item in the receipt. $line_item_display_data will be passed (and must be returned) with the following keys: - inner_html: the HTML text that will go inside a <tr> element, note that wp_kses_post will be applied to this text before actual rendering. - tr_attributes: attributes (e.g. 'class', 'data', 'style') that will be applied to the <tr> element, as an associative array of attribute name => value. - row_index: a number that starts at 0 and increases by one for each processed line item. $line_item_data will contain the following keys: - type: One of 'product', 'subtotal', 'discount', 'fee', 'shipping_total', 'taxes_total', 'amount_paid' - title - amount (formatted with wc_price) - item (only when type is 'product'), and instance of WC_Order_Item - quantity (only when type is 'product')

### woocommerce_privacy_erase_order_personal_data
**Args:** $erasure_enabled, $order
**Tags:** #filter

### woocommerce_privacy_export_order_personal_data
**Params:** array $personal_data, WC_Order $order
**Since:** 3.4.0 | **Tags:** #filter
Allow extensions to register their own personal data for this order for the export.

### woocommerce_privacy_export_order_personal_data_meta
**Args:** array(
				'Payer first name'     => __( 'Payer first name', 'woocommerce' ),
				'Payer last name'      => __( 'Payer last name', 'woocommerce' ),
				'Payer PayPal address' => __( 'Payer PayPal address', 'woocommerce' ),
				'Transaction ID'       => __( 'Transaction ID', 'woocommerce' ),
			)
**Tags:** #filter

### woocommerce_privacy_export_order_personal_data_meta_value
**Args:** $order->get_meta( $meta_key ), $meta_key, $order
**Tags:** #filter

### woocommerce_privacy_export_order_personal_data_prop
**Args:** $value, $prop, $order
**Tags:** #filter

### woocommerce_privacy_export_order_personal_data_props
**Args:** array(
				'order_number'               => __( 'Order Number', 'woocommerce' ),
				'date_created'               => __( 'Order Date', 'woocommerce' ),
				'total'                      => __( 'Order Total', 'woocommerce' ),
				'items'                      => __( 'Items Purchased', 'woocommerce' ),
				'customer_ip_address'        => __( 'IP Address', 'woocommerce' ),
				'customer_user_agent'        => __( 'Browser User Agent', 'woocommerce' ),
				'formatted_billing_address'  => __( 'Billing Address', 'woocommerce' ),
				'formatted_shipping_address' => __( 'Shipping Address', 'woocommerce' ),
				'billing_phone'              => __( 'Phone Number', 'woocommerce' ),
				'billing_email'              => __( 'Email Address', 'woocommerce' ),
				'shipping_phone'             => __( 'Shipping Phone Number', 'woocommerce' ),
			), $order
**Tags:** #filter

### woocommerce_privacy_remove_order_personal_data_meta
**Args:** array(
				'Payer first name'     => 'text',
				'Payer last name'      => 'text',
				'Payer PayPal address' => 'email',
				'Transaction ID'       => 'numeric_id',
			)
**Tags:** #filter

### woocommerce_privacy_remove_order_personal_data_meta_value
**Params:** string $anon_value, string $prop, string $value, string $data_type, WC_Order $order
**Since:** 3.4.0 | **Tags:** #filter
Expose a way to control the anonymized value of a value via 3rd party code.

### woocommerce_privacy_remove_order_personal_data_prop_value
**Params:** string $anon_value, string $prop, string $value, string $data_type, WC_Order $order
**Since:** 3.4.0 | **Tags:** #filter
Expose a way to control the anonymized value of a prop via 3rd party code.

### woocommerce_privacy_remove_order_personal_data_props
**Params:** array $props, WC_Order $order
**Since:** 3.4.0 | **Tags:** #filter
Expose props and data types we'll be anonymizing.

### woocommerce_redirect_order_location
**Params:** string $redirect_to, int $order_id, \WC_Order $order
**Since:** 8.0.0 | **Tags:** #filter
Filter the URL used to redirect after an order is updated. Similar to the WP post's `redirect_post_location` filter.

### woocommerce_refund_restock_note
**Params:** string $restock_note, int $old_stock, bool|int|null $new_stock, WC_Order $order, bool|WC_Product $product
**Since:** 6.4.0 | **Tags:** #filter
Allow the restock note to be modified.

### woocommerce_report_orders_export_columns
**Args:** $export_columns
**Tags:** #filter

### woocommerce_report_orders_prepare_export_item
**Args:** $export_item, $item
**Tags:** #filter

### woocommerce_reports_get_order_report_data
**Args:** $wpdb->$query_type( $query ), $data
**Tags:** #filter

### woocommerce_reports_get_order_report_data_args
**Args:** $args
**Tags:** #filter

### woocommerce_reports_get_order_report_query
**Args:** $query
**Tags:** #filter

### woocommerce_reports_order_statuses
**Params:** string[] $order_statuses
**Since:** 2.2.0 | **Tags:** #filter
Allows modifying the order statuses used in the top seller query inside the dashboard status widget.

### woocommerce_sort_fees_callback
**Params:** stdClass $a, stdClass $b
**Since:** 3.8.0 | **Tags:** #filter
Filter sort fees callback.

### woocommerce_structured_data_order
**Args:** $markup, $sent_to_admin, $order
**Tags:** #filter

### woocommerce_thankyou_order_received_title
**Params:** string $title, WC_Order|false $order
**Since:** 9.6.0 | **Tags:** #filter
Filter the title shown after a checkout is complete.

### woocommerce_trash_cancelled_orders_query_args
**Args:** array(
					'date_created' => '<' . strtotime( '-' . $option['number'] . ' ' . $option['unit'] ),
					'limit'        => $limit, // Batches of 20.
					'status'       => OrderInternalStatus::CANCELLED,
					'type'         => 'shop_order',
				)
**Tags:** #filter

### woocommerce_trash_failed_orders_query_args
**Args:** array(
					'date_created' => '<' . strtotime( '-' . $option['number'] . ' ' . $option['unit'] ),
					'limit'        => $limit, // Batches of 20.
					'status'       => OrderInternalStatus::FAILED,
					'type'         => 'shop_order',
				)
**Tags:** #filter

### woocommerce_trash_pending_orders_query_args
**Args:** array(
					'date_created' => '<' . strtotime( '-' . $option['number'] . ' ' . $option['unit'] ),
					'limit'        => $limit, // Batches of 20.
					'status'       => OrderInternalStatus::PENDING,
					'type'         => 'shop_order',
				)
**Tags:** #filter

### woocommerce_update_order_review_fragments
**Args:** array(
						'form.woocommerce-checkout' => wc_print_notice(
							esc_html__( 'Sorry, your session has expired.', 'woocommerce' ) . ' <a href="' . esc_url( wc_get_page_permalink( 'shop' ) ) . '" class="wc-backward">' . esc_html__( 'Return to shop', 'woocommerce' ) . '</a>',
							'error',
							array(),
							true
						),
					)
**Tags:** #filter

### woocommerce_valid_order_statuses_for_cancel
**Params:** array $valid_statuses, WC_Order $order
**Since:** 3.5.0 | **Tags:** #filter
Filter valid order statuses for cancel.

### woocommerce_valid_order_statuses_for_payment
**Params:** array $valid_order_statuses, WC_Order $order
**Since:** 4.0.0 | **Tags:** #filter
Filter the valid order statuses for payment.

### woocommerce_valid_order_statuses_for_payment_complete
**Params:** array $valid_completed_statuses, WC_Order $this
**Since:** 2.7.0 | **Tags:** #filter
Filters the valid order statuses for payment complete.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
