# WooCommerce Actions: Other

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_add_payment_method_form_bottom
**Tags:** #action

### woocommerce_archive_description
**Tags:** #action

### woocommerce_available_download_end
**Args:** $download
**Tags:** #action

### woocommerce_available_download_start
**Args:** $download
**Tags:** #action

### woocommerce_lostpassword_form
**Tags:** #action

### woocommerce_resetpassword_form
**Tags:** #action

### woocommerce_review_after_comment_text
**Args:** $comment
**Tags:** #action

### woocommerce_review_before
**Args:** $comment
**Tags:** #action

### woocommerce_review_before_comment_meta
**Args:** $comment
**Tags:** #action

### woocommerce_review_before_comment_text
**Args:** $comment
**Tags:** #action

### woocommerce_review_comment_text
**Args:** $comment
**Tags:** #action

### woocommerce_review_meta
**Args:** $comment
**Tags:** #action

### woocommerce_share
**Tags:** #action

### woocommerce_thankyou
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_thankyou_$ORDER->GET_PAYMENT_METHOD
**Tags:** #action

### after_woocommerce_add_payment_method
**Tags:** #action

### after_woocommerce_pay
**Tags:** #action

### before_woocommerce_add_payment_method
**Tags:** #action

### before_woocommerce_pay
**Params:** int $order_id
**Tags:** #action
Show the pay page.

### before_woocommerce_pay_form
**Params:** WC_Order $order, string $order_button_text, array $available_gateways
**Since:** 6.6 | **Tags:** #action
Triggered right before the Pay for Order form, after validation of the order and customer.

### lostpassword_post
**Args:** $errors, $user_data
**Tags:** #action

### password_reset
**Params:** WP_User $user, string $new_pass
**Since:** 9.4.0 | **Tags:** #action
Handles resetting the user's password.

### retrieve_password
**Args:** $user_login
**Tags:** #action

### woocommerce_delete_$POST_TYPE
**Tags:** #action

### woocommerce_new_payment_token
**Args:** $token_id, $token
**Tags:** #action

### woocommerce_new_webhook
**Args:** $webhook_id, $webhook
**Tags:** #action

### woocommerce_payment_token_deleted
**Args:** $token->get_id(), $token
**Tags:** #action

### woocommerce_payment_token_loaded
**Args:** $token
**Tags:** #action

### woocommerce_payment_token_object_updated_props
**Args:** $token, $updated_props
**Tags:** #action

### woocommerce_payment_token_updated
**Args:** $token->get_id()
**Tags:** #action

### woocommerce_trash_$POST_TYPE
**Tags:** #action

### woocommerce_webhook_deleted
**Args:** $webhook->get_id(), $webhook
**Tags:** #action

### woocommerce_webhook_loaded
**Args:** $webhook
**Tags:** #action

### woocommerce_webhook_updated
**Args:** $webhook->get_id()
**Tags:** #action

### $action
**Tags:** #action

### $hook
**Tags:** #action

### $old_hook
**Tags:** #action

### CONTROLLER->GET_HOOK_PREFIXcreated
**Tags:** #action

### CONTROLLER->GET_HOOK_PREFIXdeleted
**Tags:** #action

### CONTROLLER->GET_HOOK_PREFIXupdated
**Tags:** #action

### added_$THIS->OBJECT_TYPE_meta
**Tags:** #action

### before_woocommerce_init
**Tags:** #action

### deleted_$THIS->OBJECT_TYPE_meta
**Tags:** #action

### deprecated_argument_run
**Params:** string $argument, string $version, string $replacement
**Since:** 3.0.0 | **Tags:** #action
Wrapper for deprecated arguments so we can apply some extra logic.

### deprecated_function_run
**Params:** string $function, string $version, string $replacement
**Since:** 3.0.0 | **Tags:** #action
Wrapper for deprecated functions so we can apply some extra logic.

### deprecated_hook_run
**Params:** string $hook, string $version, string $replacement, string $message
**Since:** 3.3.0 | **Tags:** #action
Wrapper for deprecated hook so we can apply some extra logic.

### doing_it_wrong_run
**Args:** $function, $message, $version
**Tags:** #action

### enqueue_block_editor_assets
**Tags:** #action

### generate_category_lookup_table
**Tags:** #action

### import_end
**Tags:** #action

### manage_$THIS->SCREEN->ID_custom_column
**Tags:** #action

### media_upload_file
**Tags:** #action

### self::FEATURE_ENABLED_CHANGED_ACTION
**Tags:** #action

### self::WEBHOOK_ACTION
**Tags:** #action

### updated_$THIS->OBJECT_TYPE_meta
**Tags:** #action

### valid-paypal-standard-ipn-request
**Args:** $posted
**Tags:** #action

### validate_password_reset
**Args:** $errors, $user
**Tags:** #action

### wc_ajax_$ACTION
**Tags:** #action

### wc_logs_load_tab
**Params:** string $view
**Since:** 8.6.0 | **Tags:** #action
Action fires when the Logs tab starts loading.

### wc_logs_render_page
**Params:** string $handler
**Since:** 8.6.0 | **Tags:** #action
Action fires only if there is not a built-in rendering method for the current default log handler. This is intended as a way for extensions to render log views for custom handlers.

### wc_migrator_batch_processed
**Params:** array $batch_results, array $source_data, array $mapped_products
**Since:** 10.3.0 | **Tags:** #action
Fires when a batch has been processed during migration.

### wc_migrator_error_occurred
**Params:** string $error_type, string $message, array $context
**Since:** 10.3.0 | **Tags:** #action
Fires when an error occurs during migration.

### wc_payment_gateways_initialized
**Params:** WC_Payment_Gateways $wc_payment_gateways
**Since:** 8.5.0 | **Tags:** #action
Hook that is called when the payment gateways have been initialized.

### wc_reports_tabs
**Tags:** #action

### woocommerce_activated_plugin
**Params:** bool $activated_plugin
**Since:** 5.0.0 | **Tags:** #action
WooCommerce is activated hook.

### woocommerce_analytics_delete_tax
**Params:** int $tax_rate_id, int $order_id
**Tags:** #action
Fires when tax's reports are removed from database.

### woocommerce_analytics_regenerate_init
**Params:** int|bool $days, bool $skip_existing
**Tags:** #action
Fires when report data regeneration begins.

### woocommerce_analytics_update_tax
**Params:** int $tax_rate_id, int $order_id
**Tags:** #action
Fires when tax's reports are updated.

### woocommerce_blocks_$THIS->REGISTRY_IDENTIFIER_registration
**Tags:** #action

### woocommerce_blocks_loaded
2.5.0
**Since:** Fires when the woocommerce blocks are loaded and ready to use. This hook is intended to be used as a safe event hook for when the plugin has been loaded, and all dependency requirements have been met. To ensure blocks are initialized, you must use the `woocommerce_blocks_loaded` hook instead of the `plugins_loaded` hook. This is because the functions hooked into plugins_loaded on the same priority load in an inconsistent and unpredictable manner. | **Tags:** #action

### woocommerce_blocks_validate_location_$LOCATION_fields
**Tags:** #action

### woocommerce_caught_exception
**Args:** $exception_object, $function, $args
**Tags:** #action

### woocommerce_cleanup_rate_limits
**Tags:** #action

### woocommerce_core_profiler_step_complete
**Params:** string $step
**Since:** 6.5.0 | **Tags:** #action
Fires when a core profiler step is completed.

### woocommerce_credit_card_form_end
**Args:** $this->id
**Tags:** #action

### woocommerce_credit_card_form_start
**Args:** $this->id
**Tags:** #action

### woocommerce_echeck_form_end
**Args:** $this->id
**Tags:** #action

### woocommerce_echeck_form_start
**Args:** $this->id
**Tags:** #action

### woocommerce_emogrifier
**Params:** CssInliner $css_inliner, WC_Email $email
**Since:** 4.1.0 | **Tags:** #action
Action hook fired when an email content has been processed by Emogrifier CssInliner instance.

### woocommerce_flush_rewrite_rules
**Tags:** #action

### woocommerce_fulfillment_after_create
**Params:** Fulfillment $data
**Since:** 10.1.0 | **Tags:** #action
Action to perform after a fulfillment is created.

### woocommerce_fulfillment_after_delete
**Args:** $data
**Tags:** #action

### woocommerce_fulfillment_after_fulfill
**Params:** Fulfillment $data
**Since:** 10.1.0 | **Tags:** #action
Action to perform after a fulfillment is fulfilled.

### woocommerce_fulfillment_after_update
**Params:** Fulfillment $data, array $changes, string $previous_status
**Since:** 10.1.0 | **Tags:** #action
Action to perform after a fulfillment is updated.

### woocommerce_fulfillment_created_notification
**Args:** $order_id, $fulfillment, wc_get_order( $order_id )
**Tags:** #action

### woocommerce_fulfillment_deleted_notification
**Args:** $order_id, $fulfillment, wc_get_order( $order_id )
**Tags:** #action

### woocommerce_fulfillment_updated_notification
**Params:** int $order_id, Fulfillment $fulfillment, \WC_Order|\WC_Order_Refund|false $order, string $customer_note
**Since:** 10.1.0 | **Tags:** #action
Trigger the fulfillment updated notification on updating a fulfillment.

### woocommerce_helper_connect_start
**Since:** Fires when the Helper connection process is initiated. | **Tags:** #action

### woocommerce_helper_connected
**Since:** Fires when the Helper connection process has completed successfully. | **Tags:** #action

### woocommerce_helper_denied
**Since:** Fires when the Helper connection process is denied/cancelled. | **Tags:** #action

### woocommerce_helper_disconnected
**Since:** Fires when the Helper has been disconnected. | **Tags:** #action

### woocommerce_helper_loaded
**Tags:** #action

### woocommerce_hide_$NAME_notice
**Tags:** #action

### woocommerce_hpos_post_record_backfilled
**Params:** \WC_Order $order
**Since:** 8.5.0 | **Tags:** #action
Fired when the backing post record for an HPOS order is backfilled after an order update.

### woocommerce_hpos_post_record_migrated_on_read
**Params:** \WC_Order $order, array $diff
**Since:** 8.5.0 | **Tags:** #action
Fired when an HPOS order is updated from its corresponding post record on read due to a difference in the data.

### woocommerce_init
**Tags:** #action

### woocommerce_installed
**Tags:** #action

### woocommerce_integrations_init
**Tags:** #action

### woocommerce_loaded
**Tags:** #action

### woocommerce_log_clear
**Args:** $handle
**Tags:** #action

### woocommerce_log_remove
**Args:** $handle, $removed
**Tags:** #action

### woocommerce_newly_installed
**Tags:** #action

### woocommerce_note_action
**Params:** string $name, Note $note
**Tags:** #action
Fires when an admin note action is taken.

### woocommerce_note_action_$TRIGGERED_ACTION->NAME
**Tags:** #action

### woocommerce_note_created
**Params:** int $note_id
**Tags:** #action
Fires when an admin note is created.

### woocommerce_note_deleted
**Params:** int $note_id
**Tags:** #action
Fires when an admin note is deleted.

### woocommerce_note_loaded
**Params:** int $note_id
**Tags:** #action
Fires when an admin note is loaded.

### woocommerce_note_updated
**Params:** int $note_id
**Tags:** #action
Fires when an admin note is updated.

### woocommerce_onboarding_profile_completed
**Tags:** #action

### woocommerce_onboarding_profile_data_updated
**Params:** array $onboarding_data, array $query_args
**Since:** 6.5.0 | **Tags:** #action
Fires when onboarding profile data is updated via the REST API.

### woocommerce_payment_gateway_enabled
**Params:** WC_Payment_Gateway $gateway
**Since:** 10.7.0 | **Tags:** #action
Fires when a payment gateway has been enabled. Used by WC_Email_Admin_Payment_Gateway_Enabled to send an admin notification email. This action is registered as a transactional email action in WC_Emails::init_transactional_emails(), which ensures WC_Emails is instantiated before the _notification variant is fired.

### woocommerce_payment_token_set_default
**Args:** $token_id, $token
**Tags:** #action

### woocommerce_plugins_activate_error
**Params:** string $slug, null|WP_Error $result
**Since:** 6.4.0 | **Tags:** #action
Action triggered when a plugin activation fails.

### woocommerce_plugins_install_after
**Args:** $slug, $source
**Tags:** #action

### woocommerce_plugins_install_api_error
**Params:** string $slug, WP_Error $api
**Since:** 6.4.0 | **Tags:** #action
Action triggered when a plugin API call failed.

### woocommerce_plugins_install_before
**Args:** $slug, $source
**Tags:** #action

### woocommerce_plugins_install_error
**Params:** string $slug, object $api, WP_Error|null $result, Plugin_Upgrader $upgrader
**Since:** 6.4.0 | **Tags:** #action
Action triggered when a plugin installation fails.

### woocommerce_process_$POST->POST_TYPE_meta
**Tags:** #action

### woocommerce_scheduled_auto_draft_delete
7.7.0
**Since:** Fires after schedueld deletion of auto-draft orders has been completed. | **Tags:** #action

### woocommerce_sections_$CURRENT_TAB
**Tags:** #action

### woocommerce_set_additional_field_value
**Params:** string $key, mixed $value, string $group, WC_Customer|WC_Order $wc_object
**Since:** 8.9.0 | **Tags:** #action
Allow reacting for saving an additional field value.

### woocommerce_setup_footer
**Tags:** #action

### woocommerce_shutdown_error
**Args:** $error
**Tags:** #action

### woocommerce_store_api_rate_limit_exceeded
**Params:** string $ip_address, string $action_id
**Since:** 8.9.0 | **Tags:** #action
Fires when the rate limit is exceeded.

### woocommerce_system_status_report
**Params:** array|WP_Error $report
**Since:** 2.4.0 | **Tags:** #action
Action fired when the WooCommerce system status report is rendered.

### woocommerce_system_status_tool_executed
**Params:** array $tool
**Tags:** #action
Fires after a WooCommerce system status tool has been executed.

### woocommerce_tax_rate_added
**Args:** $tax_rate_id, $tax_rate
**Tags:** #action

### woocommerce_tax_rate_deleted
**Args:** $tax_rate_id
**Tags:** #action

### woocommerce_tax_rate_updated
**Args:** $tax_rate_id, $tax_rate
**Tags:** #action

### woocommerce_theme_installed
**Params:** string $theme
**Tags:** #action
Fires when a theme is successfully installed.

### woocommerce_tracker_send_event
**Tags:** #action

### woocommerce_transient_file_contents_served
**Params:** array $transient_file_info, bool $is_json_rest_api_request
**Since:** 8.5.0 | **Tags:** #action
Action that fires after a transient file has been successfully served, right before terminating the request.

### woocommerce_update_non_option_setting
**Args:** array(
								'id'    => $key,
								'type'  => $field['type'],
								'value' => $this->settings[ $key ],
							)
**Tags:** #action

### woocommerce_update_option
**Args:** array( 'id' => $option_key )
**Tags:** #action

### woocommerce_update_option_sanitize_title$OPTION[type]
**Tags:** #action

### woocommerce_update_options
**Tags:** #action

### woocommerce_update_options_$CURRENT_TAB
**Tags:** #action

### woocommerce_update_options_$THIS->ID_$SECTION_ID
**Tags:** #action

### woocommerce_update_options_payment_gateways_$GATEWAY->ID
**Tags:** #action

### woocommerce_updated
**Tags:** #action

### woocommerce_updated_instance_ids
**Args:** $changes
**Tags:** #action

### woocommerce_validate_additional_field
**Params:** WP_Error $errors, string $field_key, mixed $field_value
**Since:** 8.7.0 | **Tags:** #action
Pass an error object to allow validation of an additional field.

### woocommerce_webhook_options
**Params:** WC_Webhook $webhook
**Tags:** #action
Fires within the webhook editor, after the Webhook Data fields have rendered.

### woocommerce_webhook_options_save
**Args:** $webhook->get_id()
**Tags:** #action

### wp_$BLOG_ID_wc_updater_cron
**Tags:** #action

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
