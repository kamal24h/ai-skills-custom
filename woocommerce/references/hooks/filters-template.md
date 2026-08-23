# WooCommerce Filters: Template

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_pagination_args
**Args:** array( // WPCS: XSS ok.
				'base'      => $base,
				'format'    => $format,
				'add_args'  => false,
				'current'   => max( 1, $current ),
				'total'     => $total,
				'prev_text' => is_rtl() ? '&rarr;' : '&larr;',
				'next_text' => is_rtl() ? '&larr;' : '&rarr;',
				'type'      => 'list',
				'end_size'  => 3,
				'mid_size'  => 3,
			)
**Tags:** #filter

### loop_shop_columns
**Args:** $columns
**Tags:** #filter

### woocommerce_breadcrumb_defaults
**Params:** array $args
**Tags:** #filter
Output the WooCommerce Breadcrumb.

### woocommerce_breadcrumb_home_url
**Args:** home_url()
**Tags:** #filter

### woocommerce_subcategory_count_html
**Args:** ' <mark class="count">(' . esc_html( $category->count ) . ')</mark>', $category
**Tags:** #filter

### woocommerce_theme_slug_for_templates
**Args:** get_option( 'template' )
**Tags:** #filter

### woocommerce_shortcode_products_query
**Args:** $query_args, $this->attributes, $this->type
**Tags:** #filter

### woocommerce_shortcode_products_query_results
**Params:** stdClass $results, WC_Shortcode_Products $this
**Since:** 4.0.0 | **Tags:** #filter
Filter shortcode products query results.

### widget_title
**Params:** string $title, array $instance, string $woo_widget_idbase
**Since:** 9.4.0 | **Tags:** #filter
Filter the widget's title.

### woocommerce_price_filter_widget_max_amount
**Args:** ceil( $max_price / $step ) * $step
**Tags:** #filter

### woocommerce_price_filter_widget_min_amount
**Args:** floor( $min_price / $step ) * $step
**Tags:** #filter

### woocommerce_price_filter_widget_step
**Args:** 10
**Tags:** #filter

### woocommerce_widget_layered_nav_term_anchor_text
**Params:** string $term_name, WP_Term $term, string $taxonomy
**Since:** 8.8.0 | **Tags:** #filter
Allows the attribute term name to be modified before being output.

### $SHORTCODE_shortcode_tag
**Tags:** #filter

### __experimental_woocommerce_$PRODUCT_TYPE_add_to_cart_with_options_block_template_part
**Tags:** #filter

### loop_shop_per_page
**Args:** wc_get_default_products_per_row() * wc_get_default_product_rows_per_page()
**Tags:** #filter

### loop_shop_post_in
**Args:** array()
**Tags:** #filter

### wc_get_template
**Params:** string $located, string $file, array $args, string $template_path, string $default_path
**Since:** 2.1.0 | **Tags:** #filter
Allow 3rd party plugins to filter the template file location.

### wc_get_template_part
**Args:** $template, $slug, $name
**Tags:** #filter

### woocommerce_before_$THIS->ORDER_TYPE_list_table_view_links
**Tags:** #filter

### woocommerce_breadcrumb_main_term
**Params:** \WP_Term $main_term, \WP_Term[] $terms
**Since:** 9.5.0 | **Tags:** #filter
Filters the main term used in product breadcrumbs.

### woocommerce_cached_widget_id
**Args:** $widget_id_for_cache
**Tags:** #filter

### woocommerce_get_breadcrumb
**Params:** array $crumbs, \WC_Breadcrumb|null $breadcrumb
**Since:** 2.3.0 | **Tags:** #filter
Filters the breadcrumb trail array.

### woocommerce_has_block_template
**Params:** boolean $has_template, string $template_name
**Since:** 10.2.0 | **Tags:** #filter
Filters the value of the result of the block template check.

### woocommerce_locate_core_template
**Args:** $core_file, $template, $this->template_base, $this->id
**Tags:** #filter

### woocommerce_locate_template
**Params:** string $template, string $template_name, string $template_path, string $template_path
**Since:** 9.5.0 | **Tags:** #filter
Filter to customize the path of a given WooCommerce template. Note: the $default_path argument was added in WooCommerce 9.5.0.

### woocommerce_navigation_get_breadcrumbs
**Params:** array $breadcrumbs, array|boolean $current_page
**Tags:** #filter
The navigation breadcrumbs for the current page.

### woocommerce_status_widget_low_in_stock_count_pre_query
**Params:** null|string $low_in_stock_count, int $stock, int $nostock
**Since:** 4.3.0 | **Tags:** #filter
Status widget low in stock count pre query.

### woocommerce_status_widget_out_of_stock_count_pre_query
**Params:** null|string $outofstock_count, int $nostock
**Since:** 4.3.0 | **Tags:** #filter
Status widget out of stock count pre query.

### woocommerce_structured_data_breadcrumblist
**Args:** $markup, $breadcrumbs
**Tags:** #filter

### woocommerce_template_directory
**Args:** 'woocommerce', $template
**Tags:** #filter

### woocommerce_template_loader_files
**Params:** string $default_file
**Since:** 3.0.0 | **Tags:** #filter
Get an array of filenames to search for a given template.

### woocommerce_template_overrides_scan_paths
**Args:** array( 'WooCommerce' => WC()->plugin_path() . '/templates/' )
**Tags:** #filter

### woocommerce_template_path
**Args:** 'woocommerce/'
**Tags:** #filter

### woocommerce_template_url
**Args:** 'woocommerce/'
**Tags:** #filter

### woocommerce_widget_get_current_page_url
**Args:** $link, $this
**Tags:** #filter

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
