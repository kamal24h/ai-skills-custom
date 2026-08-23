# WooCommerce Filters: Customer

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_create_account_default_checked
**Args:** false
**Tags:** #filter

### woocommerce_lost_password_confirmation_message
**Args:** esc_html__( 'A password reset email has been sent to the email address on file for your account, but may take several minutes to show up in your inbox. Please wait at least 10 minutes before attempting another reset.', 'woocommerce' )
**Tags:** #filter

### woocommerce_lost_password_message
**Args:** esc_html__( 'Lost your password? Please enter your username or email address. You will receive a link to create a new password via email.', 'woocommerce' )
**Tags:** #filter

### woocommerce_my_account_edit_address_title
**Args:** $page_title, $load_address
**Tags:** #filter

### woocommerce_my_account_get_addresses
**Args:** array(
			'billing'  => __( 'Billing address', 'woocommerce' ),
			'shipping' => __( 'Shipping address', 'woocommerce' ),
		), $customer_id
**Tags:** #filter

### woocommerce_my_account_my_address_description
**Args:** esc_html__( 'The following addresses will be used on the checkout page by default.', 'woocommerce' )
**Tags:** #filter

### woocommerce_my_account_my_downloads_title
**Args:** esc_html__( 'Available downloads', 'woocommerce' )
**Tags:** #filter

### woocommerce_my_account_my_orders_columns
**Args:** array(
		'order-number'  => esc_html__( 'Order', 'woocommerce' ),
		'order-date'    => esc_html__( 'Date', 'woocommerce' ),
		'order-status'  => esc_html__( 'Status', 'woocommerce' ),
		'order-total'   => esc_html__( 'Total', 'woocommerce' ),
		'order-actions' => '&nbsp;',
	)
**Tags:** #filter

### woocommerce_my_account_my_orders_query
**Args:** array(
					'customer' => get_current_user_id(),
					'page'     => $current_page,
					'paginate' => true,
				)
**Tags:** #filter

### woocommerce_my_account_my_orders_title
**Args:** esc_html__( 'Recent orders', 'woocommerce' )
**Tags:** #filter

### woocommerce_reset_password_message
**Args:** esc_html__( 'Enter a new password below.', 'woocommerce' )
**Tags:** #filter

### woocommerce_account_endpoint_page_not_found
**Args:** true
**Tags:** #filter

### woocommerce_logout_default_redirect_url
**Params:** string $logout_url
**Since:** 2.6.9 | **Tags:** #filter
Filters the logout redirect URL.

### woocommerce_my_account_edit_address_field_value
**Args:** $value, $key, $load_address
**Tags:** #filter

### woocommerce_my_account_message
**Args:** ''
**Since:** 2.6.0 | **Tags:** #filter
Filters the message shown on the 'my account' page when the user is not logged in.

### woocommerce_customer_allowed_session_meta_keys
**Params:** array $allowed_keys, WC_Customer $customer
**Since:** 8.7.0 | **Tags:** #filter
Filter the allowed session meta data keys. If the customer object contains any meta data with these keys, it will be stored within the WooCommerce session.

### woocommerce_customer_get_last_order
**Params:** string $last_order_id, WC_Customer $customer
**Since:** 4.9.1 | **Tags:** #filter
Filters the id of the last order from a given customer.

### woocommerce_customer_get_order_count
**Params:** mixed $order_count, WC_Customer $customer
**Since:** 4.9.0 | **Tags:** #filter
Filters total orders count value for a given customer.

### woocommerce_customer_get_total_spent
**Params:** mixed $money_spent, WC_Customer $customer
**Since:** 3.1.0 | **Tags:** #filter
Filters total spent value for a given customer.

### woocommerce_customer_get_total_spent_query
**Params:** string $sql, WC_Customer $customer
**Since:** 3.1.0 | **Tags:** #filter
Filters the SQL query used to get the combined total of all the orders from a given customer.

### woocommerce_customer_pre_search_customers
**Args:** false, $term, $limit
**Tags:** #filter

### woocommerce_customer_query_args
**Params:** array $query_args, array $args
**Since:** 10.4.0 | **Tags:** #filter
Filter customer query args before execution.

### woocommerce_customer_search_customers
**Args:** array(
					'search'         => '*' . esc_attr( $term ) . '*',
					'search_columns' => array( 'user_login', 'user_url', 'user_email', 'user_nicename', 'display_name' ),
					'fields'         => 'ID',
					'number'         => $limit,
				), $term, $limit, 'main_query'
**Tags:** #filter

### woocommerce_downloadable_file_permission_data
**Args:** $data
**Tags:** #filter

### woocommerce_downloadable_file_permission_format
**Args:** $format, $data
**Tags:** #filter

### woocommerce_update_customer_args
**Params:** WC_Customer $customer
**Since:** 3.0.0 | **Tags:** #filter
Updates a customer in the database.

### illegal_user_logins
**Params:** array $usernames
**Since:** 3.7.0 | **Tags:** #filter
WordPress 4.4 - filters the list of blocked usernames.

### users_have_additional_content
**Args:** false, $userids
**Tags:** #filter

### wc_session_expiration
**Params:** int $expiration_seconds
**Since:** 5.0.0 | **Tags:** #filter
Filters the session expiration.

### wc_session_expiring
**Params:** int $expiration_seconds
**Since:** 5.0.0 | **Tags:** #filter
Filters the session expiration.

### wc_session_use_secure_cookie
**Params:** bool $use_secure_cookie
**Since:** 3.6.0 | **Tags:** #filter
Filter whether to use a secure cookie.

### woocommerce_account_downloads_columns
**Args:** array(
			'download-product'   => __( 'Product', 'woocommerce' ),
			'download-remaining' => __( 'Downloads remaining', 'woocommerce' ),
			'download-expires'   => __( 'Expires', 'woocommerce' ),
			'download-file'      => __( 'Download', 'woocommerce' ),
			'download-actions'   => '&nbsp;',
		)
**Tags:** #filter

### woocommerce_account_menu_item_classes
**Args:** $classes, $endpoint
**Tags:** #filter

### woocommerce_account_menu_items
**Args:** $items, $endpoints
**Tags:** #filter

### woocommerce_account_orders_columns
**Params:** array $columns
**Since:** 2.6.0 | **Tags:** #filter
Filters the array of My Account > Orders columns.

### woocommerce_account_payment_methods_columns
**Args:** array(
			'method'  => __( 'Method', 'woocommerce' ),
			'expires' => __( 'Expires', 'woocommerce' ),
			'actions' => '&nbsp;',
		)
**Tags:** #filter

### woocommerce_ajax_get_customer_details
**Args:** $data, $customer, $user_id
**Tags:** #filter

### woocommerce_analytics_customer_roles
**Args:** array( 'customer' )
**Tags:** #filter

### woocommerce_analytics_customers_query_args
**Args:** array(
					'orderby'      => 'total_spend',
					'order'        => 'desc',
					'order_after'  => $after,
					'order_before' => $before,
					'per_page'     => $per_page,
				)
**Tags:** #filter

### woocommerce_analytics_customers_stats_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_customers_stats_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_import_customer_roles
**Params:** int $limit, int $page, int|bool $days, bool $skip_existing
**Tags:** #filter
Get the customer IDs and total count that need to be synced.

### woocommerce_bacs_account_fields
**Args:** array(
						'bank_name'      => array(
							'label' => __( 'Bank', 'woocommerce' ),
							'value' => $bacs_account->bank_name,
						),
						'account_number' => array(
							'label' => __( 'Account number', 'woocommerce' ),
							'value' => $bacs_account->account_number,
						),
						'sort_code'      => array(
							'label' => $sortcode,
							'value' => $bacs_account->sort_code,
						),
						'iban'           => array(
							'label' => __( 'IBAN', 'woocommerce' ),
							'value' => $bacs_account->iban,
						),
						'bic'            => array(
							'label' => __( 'BIC', 'woocommerce' ),
							'value' => $bacs_account->bic,
						),
					), $order_id
**Tags:** #filter

### woocommerce_bacs_accounts
**Args:** $this->account_details, $order_id
**Tags:** #filter

### woocommerce_current_user_can_edit_customer_meta_fields
**Params:** WP_User $user
**Tags:** #filter
Show Address Fields on edit user pages.

### woocommerce_customer_available_downloads
**Args:** $downloads, $customer_id
**Tags:** #filter

### woocommerce_customer_bought_product_use_lookup_tables
**Params:** bool $enabled, string $customer_email, int $user_id, int $product_id
**Since:** 9.7.0 | **Tags:** #filter
Whether to use lookup tables - it can optimize performance, but correctness depends on the frequency of the AS job.

### woocommerce_customer_default_location
**Params:** string $default_location_string
**Since:** 2.3.0 | **Tags:** #filter
Filter the customer default location before geolocation.

### woocommerce_customer_default_location_array
**Params:** array $customer_location
**Since:** 2.3.0 | **Tags:** #filter
Filter the customer default location after geolocation.

### woocommerce_customer_edit_account_url
**Args:** $edit_account_url
**Tags:** #filter

### woocommerce_customer_get_downloadable_products
**Args:** $downloads
**Tags:** #filter

### woocommerce_customer_meta_fields
**Args:** array(
					'billing'  => array(
						'title'  => __( 'Customer billing address', 'woocommerce' ),
						'fields' => array(
							'billing_first_name' => array(
								'label'       => __( 'First name', 'woocommerce' ),
								'description' => '',
							),
							'billing_last_name'  => array(
								'label'       => __( 'Last name', 'woocommerce' ),
								'description' => '',
							),
							'billing_company'    => array(
								'label'       => __( 'Company', 'woocommerce' ),
								'description' => '',
							),
							'billing_address_1'  => array(
								'label'       => __( 'Address line 1', 'woocommerce' ),
								'description' => '',
							),
							'billing_address_2'  => array(
								'label'       => __( 'Address line 2', 'woocommerce' ),
								'description' => '',
							),
							'billing_city'       => array(
								'label'       => __( 'City', 'woocommerce' ),
								'description' => '',
							),
							'billing_postcode'   => array(
								'label'       => __( 'Postcode / ZIP', 'woocommerce' ),
								'description' => '',
							),
							'billing_country'    => array(
								'label'       => __( 'Country / Region', 'woocommerce' ),
								'description' => '',
								'class'       => 'js_field-country',
								'type'        => 'select',
								'options'     => array( '' => __( 'Select a country / region&hellip;', 'woocommerce' ) ) + WC()->countries->get_allowed_countries(),
							),
							'billing_state'      => array(
								'label'       => __( 'State / County', 'woocommerce' ),
								'description' => __( 'State / County or state code', 'woocommerce' ),
								'class'       => 'js_field-state',
							),
							'billing_phone'      => array(
								'label'       => __( 'Phone', 'woocommerce' ),
								'description' => '',
							),
							'billing_email'      => array(
								'label'       => __( 'Email address', 'woocommerce' ),
								'description' => '',
							),
						),
					),
					'shipping' => array(
						'title'  => __( 'Customer shipping address', 'woocommerce' ),
						'fields' => array(
							'copy_billing'        => array(
								'label'       => __( 'Copy from billing address', 'woocommerce' ),
								'description' => '',
								'class'       => 'js_copy-billing',
								'type'        => 'button',
								'text'        => __( 'Copy', 'woocommerce' ),
							),
							'shipping_first_name' => array(
								'label'       => __( 'First name', 'woocommerce' ),
								'description' => '',
							),
							'shipping_last_name'  => array(
								'label'       => __( 'Last name', 'woocommerce' ),
								'description' => '',
							),
							'shipping_company'    => array(
								'label'       => __( 'Company', 'woocommerce' ),
								'description' => '',
							),
							'shipping_address_1'  => array(
								'label'       => __( 'Address line 1', 'woocommerce' ),
								'description' => '',
							),
							'shipping_address_2'  => array(
								'label'       => __( 'Address line 2', 'woocommerce' ),
								'description' => '',
							),
							'shipping_city'       => array(
								'label'       => __( 'City', 'woocommerce' ),
								'description' => '',
							),
							'shipping_postcode'   => array(
								'label'       => __( 'Postcode / ZIP', 'woocommerce' ),
								'description' => '',
							),
							'shipping_country'    => array(
								'label'       => __( 'Country / Region', 'woocommerce' ),
								'description' => '',
								'class'       => 'js_field-country',
								'type'        => 'select',
								'options'     => array( '' => __( 'Select a country / region&hellip;', 'woocommerce' ) ) + WC()->countries->get_allowed_countries(),
							),
							'shipping_state'      => array(
								'label'       => __( 'State / County', 'woocommerce' ),
								'description' => __( 'State / County or state code', 'woocommerce' ),
								'class'       => 'js_field-state',
							),
							'shipping_phone'      => array(
								'label'       => __( 'Phone', 'woocommerce' ),
								'description' => '',
							),
						),
					),
				)
**Tags:** #filter

### woocommerce_customer_stock_notification_should_skip_sending
**Params:** bool $should_skip, int $notification_id
**Since:** 10.2.0 | **Tags:** #filter
Filter: woocommerce_customer_stock_notification_should_skip_sending

### woocommerce_customer_stock_notification_throttle_threshold
**Params:** int $threshold
**Since:** 10.2.0 | **Tags:** #filter
Filter: woocommerce_customer_stock_notification_throttle_threshold

### woocommerce_customer_stock_notification_unsubscribe_redirect_url
**Params:** string $url
**Since:** 10.2.0 | **Tags:** #filter
`woocommerce_customer_stock_notification_unsubscribe_redirect_url` filter.

### woocommerce_customer_stock_notification_verified_redirect_url
**Params:** string $url
**Since:** 10.2.0 | **Tags:** #filter
`woocommerce_customer_stock_notification_verified_redirect_url` filter.

### woocommerce_customer_stock_notifications_account_required_message_html
**Params:** string|null $pre, WC_Product $product
**Since:** 10.2.0 | **Tags:** #filter
Filter the account required message HTML.

### woocommerce_customer_stock_notifications_already_signed_up_message_html
**Params:** string|null $pre, WC_Product $product, Notification $notification
**Since:** 10.2.0 | **Tags:** #filter
Filter the already signed up message HTML.

### woocommerce_customer_stock_notifications_batch_size
**Params:** int $batch_size
**Since:** 10.2.0 | **Tags:** #filter
Filter: woocommerce_customer_stock_notifications_batch_size

### woocommerce_customer_stock_notifications_first_batch_delay
**Params:** int $delay, int $product_id
**Since:** 10.2.0 | **Tags:** #filter
Filter: woocommerce_customer_stock_notifications_first_batch_delay

### woocommerce_customer_stock_notifications_next_batch_delay
**Params:** int $delay, int $product_id
**Since:** 10.2.0 | **Tags:** #filter
Filter: woocommerce_customer_stock_notifications_next_batch_delay

### woocommerce_customer_stock_notifications_personalization_enabled
**Params:** bool $enabled
**Since:** 10.2.0 | **Tags:** #filter
Filter whether personalization is enabled while rendering the form.

### woocommerce_customer_stock_notifications_product_is_valid
**Params:** bool $is_valid, WC_Product $product
**Since:** 10.2.0 | **Tags:** #filter
Filter: woocommerce_customer_stock_notifications_product_is_valid Allows custom validation for whether a product is generally eligible for notifications.

### woocommerce_customer_stock_notifications_requires_nonce_check
**Params:** bool $requires_nonce_check
**Since:** 10.2.0 | **Tags:** #filter
Filter to require nonce check.

### woocommerce_customer_stock_notifications_settings
**Params:** array $default_customer_stock_notifications_settings
**Since:** 10.2.0 | **Tags:** #filter
Filter the Customer Stock Notifications settings.

### woocommerce_customer_stock_notifications_supported_product_stock_statuses
**Tags:** #filter

### woocommerce_customer_stock_notifications_supported_product_types
**Params:** array $product_types
**Since:** 10.2.0 | **Tags:** #filter
Filter: woocommerce_customer_stock_notifications_supported_product_types

### woocommerce_customer_stock_notifications_supported_stock_statuses
**Params:** array $stock_statuses
**Since:** 10.2.0 | **Tags:** #filter
Filter: woocommerce_customer_stock_notifications_supported_stock_statuses

### woocommerce_customer_stock_notifications_verification_expiration_time_threshold
**Params:** int $threshold
**Since:** 10.2.0 | **Tags:** #filter
Filter the verification codes expiration time (in seconds).

### woocommerce_customer_taxable_address
**Params:** array $taxable_address, object $customer
**Since:** 3.0.0 | **Tags:** #filter
Filters the taxable address for a given customer.

### woocommerce_delete_inactive_account_roles
**Args:** array(
						'Customer',
						'Subscriber',
					)
**Tags:** #filter

### woocommerce_download_file_xsendfile_file_path
**Args:** $parsed_file_path['file_path'], $file_path, $filename, $parsed_file_path
**Tags:** #filter

### woocommerce_download_file_xsendfile_lighttpd_file_path
**Args:** $parsed_file_path['file_path'], $file_path, $filename, $parsed_file_path
**Tags:** #filter

### woocommerce_download_file_xsendfile_x_accel_redirect_file_path
**Args:** $xsendfile_path, $file_path, $filename, $parsed_file_path
**Tags:** #filter

### woocommerce_download_parse_file_path
**Args:** $file_path, $remote_file
**Tags:** #filter

### woocommerce_download_parse_remote_file_path
**Args:** $file_path
**Tags:** #filter

### woocommerce_download_product_filepath
**Params:** string $file_path, string $email_address, WC_Order|bool $order, WC_Product $product, WC_Customer_Download $download
**Since:** 4.0.0 | **Tags:** #filter
Filter download filepath.

### woocommerce_downloadable_file_allowed_mime_types
**Args:** get_allowed_mime_types()
**Tags:** #filter

### woocommerce_downloadable_file_exists
**Args:** file_exists( $file_url ), $this->get_file()
**Tags:** #filter

### woocommerce_downloadable_file_permission
**Args:** $download, $product, $order, $qty, $item
**Tags:** #filter

### woocommerce_downloadable_products_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_generated_customer_username
**Args:** 'woo_user_' . zeroise( wp_rand( 0, 9999 ), 4 ), $email, $new_user_args, $suffix
**Tags:** #filter

### woocommerce_get_customer_payment_tokens
**Args:** $tokens, $customer_id, $gateway_id
**Tags:** #filter

### woocommerce_get_customer_payment_tokens_limit
**Args:** get_option( 'posts_per_page' )
**Tags:** #filter

### woocommerce_is_account_page
**Args:** false
**Tags:** #filter

### woocommerce_json_search_found_customers
**Args:** array( $user_string )
**Tags:** #filter

### woocommerce_login_credentials
**Args:** $creds
**Tags:** #filter

### woocommerce_login_redirect
**Args:** $redirect, $user
**Tags:** #filter

### woocommerce_my_account_my_address_formatted_address
**Args:** $address, $customer->get_id(), $address_type
**Tags:** #filter

### woocommerce_my_account_my_orders_actions
**Params:** array $actions, WC_Order $order
**Since:** 2.0.0 | **Tags:** #filter
Filters the actions available for an order on the My Account orders list.

### woocommerce_my_account_shortcode_tag
**Args:** 'woocommerce_my_account'
**Tags:** #filter

### woocommerce_new_customer_data
**Params:** array $customer_data
**Since:** 7.2.0 | **Tags:** #filter
Filters customer data before a customer account is registered. This hook filters customer data. It allows user data to be changed, for example, username, password, email, first name, last name, and role.

### woocommerce_new_customer_username
**Params:** string $username, string $email, array $new_user_args, string $suffix
**Since:** 3.7.0 | **Tags:** #filter
Filter new customer username.

### woocommerce_payment_methods_list_item
**Args:** $list[ $type ][ $key ], $payment_token
**Tags:** #filter

### woocommerce_payment_methods_types
**Args:** array(
			'cc'     => __( 'Credit card', 'woocommerce' ),
			'echeck' => __( 'eCheck', 'woocommerce' ),
		)
**Tags:** #filter

### woocommerce_paypal_account_restriction_notices_enabled
**Params:** bool $enabled
**Since:** 10.4.0 | **Tags:** #filter
Filters whether account restriction notices should be enabled. This filter allows extensions to opt out of the account restriction notice functionality.

### woocommerce_pre_customer_bought_product
**Args:** null, $customer_email, $user_id, $product_id
**Tags:** #filter

### woocommerce_privacy_erase_customer_personal_data_prop
**Args:** $erased, $prop, $customer
**Tags:** #filter

### woocommerce_privacy_erase_customer_personal_data_props
**Args:** array(
				'billing_first_name'  => __( 'Billing First Name', 'woocommerce' ),
				'billing_last_name'   => __( 'Billing Last Name', 'woocommerce' ),
				'billing_company'     => __( 'Billing Company', 'woocommerce' ),
				'billing_address_1'   => __( 'Billing Address 1', 'woocommerce' ),
				'billing_address_2'   => __( 'Billing Address 2', 'woocommerce' ),
				'billing_city'        => __( 'Billing City', 'woocommerce' ),
				'billing_postcode'    => __( 'Billing Postal/Zip Code', 'woocommerce' ),
				'billing_state'       => __( 'Billing State', 'woocommerce' ),
				'billing_country'     => __( 'Billing Country / Region', 'woocommerce' ),
				'billing_phone'       => __( 'Billing Phone Number', 'woocommerce' ),
				'billing_email'       => __( 'Email Address', 'woocommerce' ),
				'shipping_first_name' => __( 'Shipping First Name', 'woocommerce' ),
				'shipping_last_name'  => __( 'Shipping Last Name', 'woocommerce' ),
				'shipping_company'    => __( 'Shipping Company', 'woocommerce' ),
				'shipping_address_1'  => __( 'Shipping Address 1', 'woocommerce' ),
				'shipping_address_2'  => __( 'Shipping Address 2', 'woocommerce' ),
				'shipping_city'       => __( 'Shipping City', 'woocommerce' ),
				'shipping_postcode'   => __( 'Shipping Postal/Zip Code', 'woocommerce' ),
				'shipping_state'      => __( 'Shipping State', 'woocommerce' ),
				'shipping_country'    => __( 'Shipping Country / Region', 'woocommerce' ),
				'shipping_phone'      => __( 'Shipping Phone Number', 'woocommerce' ),
			), $customer
**Tags:** #filter

### woocommerce_privacy_erase_personal_data_customer
**Params:** array $response, WC_Customer $customer
**Since:** 3.4.0 | **Tags:** #filter
Allow extensions to remove data for this customer and adjust the response.

### woocommerce_privacy_export_customer_personal_data
**Params:** array $personal_data, WC_Order $order
**Since:** 3.4.0 | **Tags:** #filter
Allow extensions to register their own personal data for this customer for the export.

### woocommerce_privacy_export_customer_personal_data_prop_value
**Args:** $value, $prop, $customer
**Tags:** #filter

### woocommerce_privacy_export_customer_personal_data_props
**Args:** array(
				'billing_first_name'  => __( 'Billing First Name', 'woocommerce' ),
				'billing_last_name'   => __( 'Billing Last Name', 'woocommerce' ),
				'billing_company'     => __( 'Billing Company', 'woocommerce' ),
				'billing_address_1'   => __( 'Billing Address 1', 'woocommerce' ),
				'billing_address_2'   => __( 'Billing Address 2', 'woocommerce' ),
				'billing_city'        => __( 'Billing City', 'woocommerce' ),
				'billing_postcode'    => __( 'Billing Postal/Zip Code', 'woocommerce' ),
				'billing_state'       => __( 'Billing State', 'woocommerce' ),
				'billing_country'     => __( 'Billing Country / Region', 'woocommerce' ),
				'billing_phone'       => __( 'Billing Phone Number', 'woocommerce' ),
				'billing_email'       => __( 'Email Address', 'woocommerce' ),
				'shipping_first_name' => __( 'Shipping First Name', 'woocommerce' ),
				'shipping_last_name'  => __( 'Shipping Last Name', 'woocommerce' ),
				'shipping_company'    => __( 'Shipping Company', 'woocommerce' ),
				'shipping_address_1'  => __( 'Shipping Address 1', 'woocommerce' ),
				'shipping_address_2'  => __( 'Shipping Address 2', 'woocommerce' ),
				'shipping_city'       => __( 'Shipping City', 'woocommerce' ),
				'shipping_postcode'   => __( 'Shipping Postal/Zip Code', 'woocommerce' ),
				'shipping_state'      => __( 'Shipping State', 'woocommerce' ),
				'shipping_country'    => __( 'Shipping Country / Region', 'woocommerce' ),
				'shipping_phone'      => __( 'Shipping Phone Number', 'woocommerce' ),
			), $customer
**Tags:** #filter

### woocommerce_process_myaccount_field_$KEY
**Tags:** #filter

### woocommerce_register_log_handlers
**Args:** array( $handler_instance )
**Tags:** #filter

### woocommerce_register_shop_order_post_statuses
**Args:** array(
				OrderInternalStatus::PENDING    => array(
					'label'                     => _x( 'Pending payment', 'Order status', 'woocommerce' ),
					'public'                    => false,
					'exclude_from_search'       => false,
					'show_in_admin_all_list'    => true,
					'show_in_admin_status_list' => true,
					/* translators: %s: number of orders */
					'label_count'               => _n_noop( 'Pending payment <span class="count">(%s)</span>', 'Pending payment <span class="count">(%s)</span>', 'woocommerce' ),
				),
				OrderInternalStatus::PROCESSING => array(
					'label'                     => _x( 'Processing', 'Order status', 'woocommerce' ),
					'public'                    => false,
					'exclude_from_search'       => false,
					'show_in_admin_all_list'    => true,
					'show_in_admin_status_list' => true,
					/* translators: %s: number of orders */
					'label_count'               => _n_noop( 'Processing <span class="count">(%s)</span>', 'Processing <span class="count">(%s)</span>', 'woocommerce' ),
				),
				OrderInternalStatus::ON_HOLD    => array(
					'label'                     => _x( 'On hold', 'Order status', 'woocommerce' ),
					'public'                    => false,
					'exclude_from_search'       => false,
					'show_in_admin_all_list'    => true,
					'show_in_admin_status_list' => true,
					/* translators: %s: number of orders */
					'label_count'               => _n_noop( 'On hold <span class="count">(%s)</span>', 'On hold <span class="count">(%s)</span>', 'woocommerce' ),
				),
				OrderInternalStatus::COMPLETED  => array(
					'label'                     => _x( 'Completed', 'Order status', 'woocommerce' ),
					'public'                    => false,
					'exclude_from_search'       => false,
					'show_in_admin_all_list'    => true,
					'show_in_admin_status_list' => true,
					/* translators: %s: number of orders */
					'label_count'               => _n_noop( 'Completed <span class="count">(%s)</span>', 'Completed <span class="count">(%s)</span>', 'woocommerce' ),
				),
				OrderInternalStatus::CANCELLED  => array(
					'label'                     => _x( 'Cancelled', 'Order status', 'woocommerce' ),
					'public'                    => false,
					'exclude_from_search'       => false,
					'show_in_admin_all_list'    => true,
					'show_in_admin_status_list' => true,
					/* translators: %s: number of orders */
					'label_count'               => _n_noop( 'Cancelled <span class="count">(%s)</span>', 'Cancelled <span class="count">(%s)</span>', 'woocommerce' ),
				),
				OrderInternalStatus::REFUNDED   => array(
					'label'                     => _x( 'Refunded', 'Order status', 'woocommerce' ),
					'public'                    => false,
					'exclude_from_search'       => false,
					'show_in_admin_all_list'    => true,
					'show_in_admin_status_list' => true,
					/* translators: %s: number of orders */
					'label_count'               => _n_noop( 'Refunded <span class="count">(%s)</span>', 'Refunded <span class="count">(%s)</span>', 'woocommerce' ),
				),
				OrderInternalStatus::FAILED     => array(
					'label'                     => _x( 'Failed', 'Order status', 'woocommerce' ),
					'public'                    => false,
					'exclude_from_search'       => false,
					'show_in_admin_all_list'    => true,
					'show_in_admin_status_list' => true,
					/* translators: %s: number of orders */
					'label_count'               => _n_noop( 'Failed <span class="count">(%s)</span>', 'Failed <span class="count">(%s)</span>', 'woocommerce' ),
				),
			)
**Tags:** #filter

### woocommerce_registration_auth_new_customer
**Args:** true, $new_customer
**Tags:** #filter

### woocommerce_report_customers_export_columns
**Args:** $export_columns
**Tags:** #filter

### woocommerce_report_customers_prepare_export_item
**Params:** object $export_item, object $item
**Since:** 4.0.0 | **Tags:** #filter
Filter the column values of an item being exported.

### woocommerce_save_account_details_required_fields
**Args:** array(
				'account_first_name'   => __( 'First name', 'woocommerce' ),
				'account_last_name'    => __( 'Last name', 'woocommerce' ),
				'account_display_name' => __( 'Display name', 'woocommerce' ),
				'account_email'        => __( 'Email address', 'woocommerce' ),
			)
**Tags:** #filter

### woocommerce_session_handler
**Args:** 'WC_Session_Handler'
**Tags:** #filter

### woocommerce_update_user_last_active_threshold
**Params:** int $threshold
**Since:** 10.7.0 | **Tags:** #filter
Enables customization of the update frequency for user last active meta by adjusting the threshold from default to custom values. Note that a lower threshold results in more frequent database writes by Woo core and, if enabled, Analytics.

### woocommerce_user_last_update_fields
**Params:** int $meta_id, int $user_id, string $meta_key, mixed $_meta_value
**Since:** 2.6.0 | **Tags:** #filter
Hooks into the update user meta function to set the user last updated timestamp.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
