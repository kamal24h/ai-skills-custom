# WooCommerce Actions: Customer

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_account_content
**Tags:** #action

### woocommerce_account_dashboard
**Tags:** #action

### woocommerce_account_downloads_column_$COLUMN_ID
**Tags:** #action

### woocommerce_account_navigation
**Tags:** #action

### woocommerce_account_payment_methods_column_$COLUMN_ID
**Tags:** #action

### woocommerce_after_account_payment_methods
**Args:** $has_methods
**Tags:** #action

### woocommerce_after_customer_login_form
**Tags:** #action

### woocommerce_after_edit_account_address_form
**Tags:** #action

### woocommerce_after_edit_account_form
**Tags:** #action

### woocommerce_after_my_account
**Tags:** #action

### woocommerce_auth_page_footer
**Tags:** #action

### woocommerce_auth_page_header
**Tags:** #action

### woocommerce_available_downloads
**Args:** $downloads
**Tags:** #action

### woocommerce_before_account_payment_methods
**Args:** $has_methods
**Tags:** #action

### woocommerce_before_customer_login_form
**Tags:** #action

### woocommerce_before_edit_account_address_form
**Tags:** #action

### woocommerce_before_edit_account_form
**Tags:** #action

### woocommerce_before_my_account
**Tags:** #action

### woocommerce_edit_account_form
**Tags:** #action

### woocommerce_edit_account_form_end
**Tags:** #action

### woocommerce_edit_account_form_fields
**Tags:** #action

### woocommerce_edit_account_form_start
**Tags:** #action

### woocommerce_edit_account_form_tag
**Tags:** #action

### woocommerce_login_form
**Tags:** #action

### woocommerce_login_form_end
**Tags:** #action

### woocommerce_login_form_start
**Tags:** #action

### woocommerce_my_account_after_my_address
**Params:** string $name
**Since:** 8.7.0 | **Tags:** #action
Used to output content after core address fields.

### woocommerce_my_account_my_orders_column_$COLUMN_ID
**Tags:** #action

### woocommerce_order_details_after_customer_address
**Params:** string $address_type, WC_Order $order
**Since:** 8.7.0 | **Tags:** #action
Action hook fired after an address in the order customer details.

### woocommerce_register_form
**Tags:** #action

### woocommerce_register_form_end
**Tags:** #action

### woocommerce_register_form_start
**Tags:** #action

### woocommerce_register_form_tag
**Tags:** #action

### woocommerce_account_$KEY_endpoint
**Tags:** #action

### woocommerce_reset_password_notification
**Args:** $user->user_login, $key
**Tags:** #action

### woocommerce_customer_loaded
**Args:** $customer
**Tags:** #action

### woocommerce_customer_object_updated_props
**Args:** $customer, $updated_props
**Tags:** #action

### woocommerce_delete_customer
**Args:** $id
**Tags:** #action

### woocommerce_new_customer
**Args:** $customer->get_id(), $customer
**Tags:** #action

### woocommerce_update_customer
**Args:** $customer->get_id(), $customer
**Tags:** #action

### wc_migrator_session_completed
**Params:** string $platform, array $final_stats
**Since:** 10.3.0 | **Tags:** #action
Fires when a migration session completes.

### wc_migrator_session_started
**Params:** string $platform, array $metadata
**Since:** 10.3.0 | **Tags:** #action
Fires when a migration session starts.

### woocommerce_analytics_delete_customer
**Params:** int $order_id
**Since:** 4.0.0 | **Tags:** #action
Fires when a customer is deleted.

### woocommerce_analytics_new_customer
**Params:** int $customer_id
**Since:** 4.0.0 | **Tags:** #action
Fires when a new report customer is created.

### woocommerce_analytics_update_customer
**Params:** int $customer_id
**Since:** 4.0.0 | **Tags:** #action
Fires when a customer is updated.

### woocommerce_created_customer
**Params:** integer $customer_id, array $new_customer_data, string $password_generated
**Since:** 7.2.0 | **Tags:** #action
Fires after a customer account has been registered. This hook fires after customer accounts are created and passes the customer data.

### woocommerce_customer_reset_password
**Args:** $user
**Tags:** #action

### woocommerce_customer_save_address
**Params:** int $user_id, string $address_type
**Since:** 8.5.0 | **Tags:** #action
Hook: woocommerce_customer_save_address. Fires after a customer address has been saved on the user profile admin screen.

### woocommerce_customer_stock_notifications_product_sync
**Params:** array $product_ids
**Since:** 10.2.0 | **Tags:** #action
Allows for additional processing of the product IDs after they have been queued.

### woocommerce_customer_stock_notifications_signup
**Params:** Notification $notification
**Since:** 10.2.0 | **Tags:** #action
Action: woocommerce_customer_stock_notifications_signup

### woocommerce_download_file_$FILE_DOWNLOAD_METHOD
**Tags:** #action

### woocommerce_download_file_force
**Args:** $file_path, $filename
**Tags:** #action

### woocommerce_download_product
**Args:** $download->get_user_email(), $download->get_order_key(), $download->get_product_id(), $download->get_user_id(), $download->get_download_id(), $download->get_order_id()
**Tags:** #action

### woocommerce_guest_session_to_user_id
**Params:** string $guest_session_id, string $user_session_id
**Since:** 8.8.0 | **Tags:** #action
Fires after a customer has logged in, and their guest session id has been deleted with its data migrated to a customer id. This hook gives extensions the chance to connect the old session id to the customer id, if the key is being used externally.

### woocommerce_load_cart_from_session
3.2.0
**Since:** Fires when cart is loaded from session. | **Tags:** #action

### woocommerce_login_failed
**Tags:** #action

### woocommerce_new_customer_note
**Args:** array(
					'order_id'      => $this->get_id(),
					'customer_note' => $commentdata['comment_content'],
				)
**Tags:** #action

### woocommerce_register_feature_definitions
**Params:** FeaturesController $features_controller
**Since:** 8.3.0 | **Tags:** #action
The action for registering features.

### woocommerce_register_post
**Params:** string $username, string $user_email, \WP_Error $errors
**Since:** 7.2.0 | **Tags:** #action
Fires before a customer account is registered. This hook fires before customer accounts are created and passes the form data (username, email) and an array of errors. This could be used to add extra validation logic and append errors to the array.

### woocommerce_register_taxonomy
**Tags:** #action

### woocommerce_save_account_details
**Params:** int $user_id
**Since:** 3.6.0 | **Tags:** #action
Hook: woocommerce_save_account_details.

### woocommerce_store_api_cart_update_customer_from_request
**Params:** \WC_Customer $customer, \WP_REST_Request $request
**Since:** 7.2.0 | **Tags:** #action
Fires when the Checkout Block/Store API updates a customer from the API request data.

### woocommerce_update_new_customer_past_order
**Args:** $order_id, $customer
**Tags:** #action

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
