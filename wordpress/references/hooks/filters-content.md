# WordPress Filters: Content / Posts / Taxonomies / Queries

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### bloginfo
**Params:** mixed $output, string $show
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the site information returned by get_bloginfo().

### category_description
**Since:** 1.2.1 | **Tags:** #Legacy

### format_to_edit
**Params:** string $content
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the text to be formatted for editing.

### list_cats
**Params:** string $element, WP_Term|null $category
**Since:** 1.2.1 | **Tags:** #Legacy
Filters a taxonomy drop-down display element. A variety of taxonomy drop-down display elements can be modified just prior to display via this filter. Filterable arguments include 'show_option_none', 'show_option_all', and various forms of the term name.

### phone_content
**Params:** string $content
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the content of the post submitted by email before saving.

### single_post_title
**Params:** string $_post_title, WP_Post $_post
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the page title for a single post.

### the_category
**Params:** string $thelist, string $separator, string $parents
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the category or list of categories.

### the_category_rss
**Params:** string $the_list, string $type
**Since:** 1.2.1 | **Tags:** #Legacy
Filters all of the post categories for display in a feed.

### the_content
**Params:** string $content
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the post content.

### the_date
**Params:** string $the_date, string $format, string $before, string $after
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the date of the post, for display.

### the_excerpt
**Params:** string $post_excerpt
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the displayed post excerpt.

### the_excerpt_rss
**Params:** string $output
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the post excerpt for a feed.

### the_time
**Params:** string $get_the_time, string $format
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the time of the post, for display.

### the_title
**Params:** string $post_title, int $post_id
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the post title.

### the_title_rss
**Params:** string $title
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the post title for use in a feed.

### the_weekday
**Params:** string $the_weekday
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the localized weekday of the post, for display.

### the_weekday_date
**Params:** string $the_weekday_date, string $before, string $after
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the localized weekday of the post, for display.

### category_feed_link
**Params:** string $link, string $feed
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the category feed link.

### category_link
**Params:** string $termlink, int $term_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the category link.

### content_save_pre
**Since:** 1.5.2 | **Tags:** #Legacy

### date_rewrite_rules
**Params:** string[] $date_rewrite
**Since:** 1.5.2 | **Tags:** #Legacy
Filters rewrite rules used for date archives. Likely date archives would include `/yyyy/`, `/yyyy/mm/`, and `/yyyy/mm/dd/`.

### day_link
**Params:** string $daylink, int $year, int $month, int $day
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the day archive permalink.

### default_content
**Params:** string $post_content, WP_Post $post
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the default post content initially used in the "Write Post" form.

### default_excerpt
**Params:** string $post_excerpt, WP_Post $post
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the default post excerpt initially used in the "Write Post" form.

### default_title
**Params:** string $post_title, WP_Post $post
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the default post title initially used in the "Write Post" form.

### excerpt_save_pre
**Since:** 1.5.2 | **Tags:** #Legacy

### feed_link
**Params:** string $output, string $feed
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the feed type permalink.

### get_comments_number
**Params:** string|int $comments_number, int $post_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the returned comment count for a post.

### get_the_excerpt
**Params:** string $post_excerpt, WP_Post $post
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the retrieved post excerpt.

### get_the_guid
**Params:** string $post_guid, int $post_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the Global Unique Identifier (guid) of the post.

### get_the_time
**Params:** string|int $the_time, string $format, WP_Post $post
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the time of the post.

### mod_rewrite_rules
**Params:** string $rules
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the list of rewrite rules formatted for output to an .htaccess file.

### month_link
**Params:** string $monthlink, int $year, int $month
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the month archive permalink.

### page_link
**Params:** string $link, int $post_id, bool $sample
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the permalink for a page.

### page_rewrite_rules
**Params:** string[] $page_rewrite
**Since:** 1.5.2 | **Tags:** #Legacy
Filters rewrite rules used for "page" post type archives.

### posts_join
**Since:** 1.5.2 | **Tags:** #Legacy

### posts_join_paged
**Since:** 1.5.2 | **Tags:** #Legacy

### posts_orderby
**Since:** 1.5.2 | **Tags:** #Legacy

### posts_where
**Since:** 1.5.2 | **Tags:** #Legacy

### posts_where_paged
**Since:** 1.5.2 | **Tags:** #Legacy

### post_comments_feed_link
**Params:** string $url
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the post comments feed permalink.

### post_link
**Params:** string $permalink, WP_Post $post, bool $leavename
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the permalink for a post. Only applies to posts with post_type of 'post'.

### post_rewrite_rules
**Params:** string[] $post_rewrite
**Since:** 1.5.2 | **Tags:** #Legacy
Filters rewrite rules used for "post" archives.

### rewrite_rules_array
**Params:** string[] $rules
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the full set of generated rewrite rules.

### root_rewrite_rules
**Params:** string[] $root_rewrite
**Since:** 1.5.2 | **Tags:** #Legacy
Filters rewrite rules used for root-level archives. Likely root-level archives would include pagination rules for the homepage as well as site-wide post feeds (e.g. `/feed/`, and `/feed/atom/`).

### search_rewrite_rules
**Params:** string[] $search_rewrite
**Since:** 1.5.2 | **Tags:** #Legacy
Filters rewrite rules used for search archives. Likely search-related archives include `/search/search+query/` as well as pagination and feed paths for a search.

### the_permalink
**Params:** string $permalink, int|WP_Post $post
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the display of the permalink for the current post.

### the_posts
**Since:** 1.5.2 | **Tags:** #Legacy

### title_save_pre
**Since:** 1.5.2 | **Tags:** #Legacy

### wp_list_pages
**Params:** string $output, array $parsed_args, WP_Post[] $pages
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the HTML output of the pages to list.

### year_link
**Params:** string $yearlink, int $year
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the year archive permalink.

### add_ping
**Params:** string $new
**Since:** 2.0 | **Tags:** #Legacy
Filters the new ping URL to add for the given post.

### get_enclosed
**Params:** string[] $pung, int $post_id
**Since:** 2.0 | **Tags:** #Legacy
Filters the list of enclosures already enclosed for the given post.

### get_pung
**Params:** string[] $pung
**Since:** 2.0 | **Tags:** #Legacy
Filters the list of already-pinged URLs for the given post.

### get_the_modified_time
**Params:** string|int|false $the_time, string $format, WP_Post|null $post
**Since:** 2.0 | **Tags:** #Legacy
Filters the localized time a post was last modified.

### get_to_ping
**Params:** string[] $to_ping
**Since:** 2.0 | **Tags:** #Legacy
Filters the list of URLs yet to ping for the given post.

### posts_groupby
**Since:** 2.0 | **Tags:** #Legacy

### posts_request
**Since:** 2.0 | **Tags:** #Legacy

### the_content_rss
**Params:** string $content
**Since:** 2.0 | **Tags:** #Legacy
Filters the post content in the context of an RSS feed.

### the_modified_time
**Params:** string|false $get_the_modified_time, string $format
**Since:** 2.0 | **Tags:** #Legacy
Filters the localized time a post was last modified, for display.

### wp_title
**Params:** string $title, string $sep, string $seplocation
**Since:** 2.0 | **Tags:** #Legacy
Filters the text of the page title.

### bloginfo_url
**Params:** string $output, string $show
**Since:** 2.0.11 | **Tags:** #Legacy
Filters the URL returned by get_bloginfo().

### preview_post_link
**Params:** string $preview_link, WP_Post $post
**Since:** 2.0.11 | **Tags:** #Legacy
Filters the URL used for a post preview.

### pre_category_nicename
**Params:** string $value
**Since:** 2.0.11 | **Tags:** #Legacy
Filters the category nicename before it is sanitized. Use the {@see 'pre_$taxonomy_$field'} hook instead.

### single_cat_title
**Params:** string $term_name
**Since:** 2.0.11 | **Tags:** #Legacy
Filters the category archive page title.

### bloginfo_rss
**Params:** string $rss_container, string $show
**Since:** 2.1 | **Tags:** #Legacy
Filters the bloginfo for display in RSS feeds.

### found_posts
**Since:** 2.1 | **Tags:** #Legacy

### found_posts_query
**Since:** 2.1 | **Tags:** #Legacy

### get_bookmarks
**Params:** array $bookmarks, array $parsed_args
**Since:** 2.1 | **Tags:** #Legacy
Filters the returned list of bookmarks. The first time the hook is evaluated in this file, it returns the cached bookmarks list. The second evaluation returns a cached bookmarks list if the link category is passed but does not exist. The third evaluation returns the full cached results.

### get_pages
**Params:** WP_Post[] $pages, array $parsed_args
**Since:** 2.1 | **Tags:** #Legacy
Filters the retrieved list of pages.

### get_the_modified_date
**Params:** string|int|false $the_time, string $format, WP_Post|null $post
**Since:** 2.1 | **Tags:** #Legacy
Filters the date a post was last modified.

### postmeta_form_limit
**Params:** int $limit
**Since:** 2.1 | **Tags:** #Legacy
Filters the number of custom fields to retrieve for the drop-down in the Custom Fields meta box.

### posts_distinct
**Since:** 2.1 | **Tags:** #Legacy

### posts_fields
**Since:** 2.1 | **Tags:** #Legacy

### post_limits
**Since:** 2.1 | **Tags:** #Legacy

### the_modified_date
**Params:** string $the_modified_date, string $format, string $before, string $after
**Since:** 2.1 | **Tags:** #Legacy
Filters the date a post was last modified, for display.

### wp_dropdown_cats
**Params:** string $output, array $parsed_args
**Since:** 2.1 | **Tags:** #Legacy
Filters the taxonomy drop-down output.

### wp_dropdown_pages
**Params:** string $output, array $parsed_args, WP_Post[] $pages
**Since:** 2.1 | **Tags:** #Legacy
Filters the HTML output of a list of pages as a dropdown.

### wp_list_categories
**Params:** string $output, array|string $args
**Since:** 2.1 | **Tags:** #Legacy
Filters the HTML output of a taxonomy list.

### wp_list_pages_excludes
**Since:** 2.1 | **Tags:** #Legacy

### _get_page_link
**Params:** string $link, int $post_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the permalink for a non-page_on_front page.

### atom_enclosure
**Params:** string $html_link_tag
**Since:** 2.2 | **Tags:** #Legacy
Filters the atom enclosure HTML link tag for the current post.

### getarchives_join
**Params:** string $sql_join, array $parsed_args
**Since:** 2.2 | **Tags:** #Legacy
Filters the SQL JOIN clause for retrieving archives.

### getarchives_where
**Params:** string $sql_where, array $parsed_args
**Since:** 2.2 | **Tags:** #Legacy
Filters the SQL WHERE clause for retrieving archives.

### get_bloginfo_rss
**Params:** string $info, string $show
**Since:** 2.2 | **Tags:** #Legacy
Filters the bloginfo for use in RSS feeds.

### get_wp_title_rss
**Params:** string $title, string $deprecated
**Since:** 2.2 | **Tags:** #Legacy
Filters the blog title for use as the feed title.

### link_category
**Params:** string $cat_name
**Since:** 2.2 | **Tags:** #Legacy
Filters the category name.

### link_title
**Since:** 2.2 | **Tags:** #Legacy

### rss_enclosure
**Params:** string $html_link_tag
**Since:** 2.2 | **Tags:** #Legacy
Filters the RSS enclosure HTML link tag for the current post.

### status_header
**Params:** string $status_header, int $code, string $description, string $protocol
**Since:** 2.2 | **Tags:** #Legacy
Filters an HTTP status header.

### the_meta_key
**Params:** string $html, string $key, string $value
**Since:** 2.2 | **Tags:** #Legacy
Filters the HTML output of the li element in the post custom fields list.

### url_to_postid
**Params:** string $url
**Since:** 2.2 | **Tags:** #Legacy
Filters the URL to derive the post ID from.

### wp_title_rss
**Params:** string $wp_title_rss, string $deprecated
**Since:** 2.2 | **Tags:** #Legacy
Filters the blog title for display of the feed title.

### edit_comment_link
**Params:** string $link, string $comment_id, string $text
**Since:** 2.3 | **Tags:** #Legacy
Filters the comment edit link anchor tag.

### edit_post_link
**Params:** string $link, int $post_id, string $text
**Since:** 2.3 | **Tags:** #Legacy
Filters the post edit link anchor tag.

### edit_post_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### edit_term_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### edit_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### edit_{$taxonomy}_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### get_comment
**Params:** WP_Comment|null $_comment
**Since:** 2.3 | **Tags:** #Legacy
Fires after a comment is retrieved.

### get_edit_comment_link
**Params:** string $location, int $comment_id, string $context
**Since:** 2.3 | **Tags:** #Legacy
Filters the comment edit link.

### get_edit_post_link
**Params:** string $link, int $post_id, string $context
**Since:** 2.3 | **Tags:** #Legacy
Filters the post edit link.

### get_lastpostdate
**Params:** string|false $lastpostdate, string $timezone, string $post_type
**Since:** 2.3 | **Tags:** #Legacy
Filters the most recent time that a post on the site was published.

### get_lastpostmodified
**Params:** string|false $lastpostmodified, string $timezone, string $post_type
**Since:** 2.3 | **Tags:** #Legacy
Filters the most recent time that a post on the site was modified.

### get_search_query
**Params:** mixed $search
**Since:** 2.3 | **Tags:** #Legacy
Filters the contents of the search query variable.

### get_tags
**Params:** WP_Term[]|int|WP_Error $tags, array $args
**Since:** 2.3 | **Tags:** #Legacy
Filters the array of term objects returned for the 'post_tag' taxonomy.

### get_term
**Params:** WP_Term $_term, string $taxonomy
**Since:** 2.3 | **Tags:** #Legacy
Filters a taxonomy term object. The {@see 'get_$taxonomy'} hook is also available for targeting a specific taxonomy.

### get_terms
**Params:** array $terms, array|null $taxonomies, array $args, WP_Term_Query $term_query
**Since:** 2.3 | **Tags:** #Legacy
Filters the found terms.

### get_the_tags
**Params:** WP_Term[]|false|WP_Error $terms
**Since:** 2.3 | **Tags:** #Legacy
Filters the array of tags for the given post.

### get_{$taxonomy}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### import_upload_size_limit
**Params:** int $max_upload_size
**Since:** 2.3 | **Tags:** #Legacy
Filters the maximum allowed upload size for import files.

### list_terms_exclusions
**Params:** string $exclusions, array $args, string[] $taxonomies
**Since:** 2.3 | **Tags:** #Legacy
Filters the terms to exclude from the terms query.

### posts_results
**Since:** 2.3 | **Tags:** #Legacy

### post_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### pre_post_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### pre_term_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### pre_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### pre_{$taxonomy}_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### single_tag_title
**Params:** string $term_name
**Since:** 2.3 | **Tags:** #Legacy
Filters the tag archive page title.

### tag_feed_link
**Params:** string $link, string $feed
**Since:** 2.3 | **Tags:** #Legacy
Filters the post tag feed link.

### tag_link
**Params:** string $termlink, int $term_id
**Since:** 2.3 | **Tags:** #Legacy
Filters the tag link.

### term_id_filter
**Params:** int $term_id, int $tt_id, array $args
**Since:** 2.3 | **Tags:** #Legacy
Filters the term ID after a new term is created.

### term_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### term_{$field}_rss
**Since:** 2.3 | **Tags:** #Variable #Legacy

### the_permalink_rss
**Params:** string $post_permalink
**Since:** 2.3 | **Tags:** #Legacy
Filters the permalink to the post for use in feeds.

### the_search_query
**Params:** mixed $search
**Since:** 2.3 | **Tags:** #Legacy
Filters the contents of the search query variable, for display.

### the_tags
**Params:** string $tag_list, string $before, string $sep, string $after, int $post_id
**Since:** 2.3 | **Tags:** #Legacy
Filters the tags list for a given post.

### wp_dropdown_users
**Params:** string $output
**Since:** 2.3 | **Tags:** #Legacy
Filters the wp_dropdown_users() HTML output.

### wp_generate_tag_cloud
**Params:** string[]|string $return, WP_Term[] $tags, array $args
**Since:** 2.3 | **Tags:** #Legacy
Filters the generated output of a tag cloud. The filter is only evaluated if a true value is passed to the $filter argument in wp_generate_tag_cloud().

### wp_tag_cloud
**Params:** string|string[] $return, array $args
**Since:** 2.3 | **Tags:** #Legacy
Filters the tag cloud output.

### {$field_no_prefix}_edit_pre
**Since:** 2.3 | **Tags:** #Variable #Legacy

### {$field_no_prefix}_save_pre
**Since:** 2.3 | **Tags:** #Variable #Legacy

### {$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### {$field}_pre
**Since:** 2.3 | **Tags:** #Variable #Legacy

### {$taxonomy}_{$field}
**Since:** 2.3 | **Tags:** #Variable #Legacy

### get_pagenum_link
**Params:** string $result, int $pagenum
**Since:** 2.5 | **Tags:** #Legacy
Filters the page number link for the current request.

### get_the_generator_{$type}
**Since:** 2.5 | **Tags:** #Variable #Legacy

### get_{$adjacent}_post_join
**Since:** 2.5 | **Tags:** #Variable #Legacy

### get_{$adjacent}_post_sort
**Since:** 2.5 | **Tags:** #Variable #Legacy

### get_{$adjacent}_post_where
**Since:** 2.5 | **Tags:** #Variable #Legacy

### htmledit_pre
**Params:** string $output
**Since:** 2.5 | **Tags:** #Legacy
Filters the text before it is formatted for the HTML editor.

### posts_distinct_request
**Since:** 2.5 | **Tags:** #Legacy

### posts_fields_request
**Since:** 2.5 | **Tags:** #Legacy

### posts_groupby_request
**Since:** 2.5 | **Tags:** #Legacy

### posts_join_request
**Since:** 2.5 | **Tags:** #Legacy

### posts_orderby_request
**Since:** 2.5 | **Tags:** #Legacy

### posts_where_request
**Since:** 2.5 | **Tags:** #Legacy

### post_limits_request
**Since:** 2.5 | **Tags:** #Legacy

### search_feed_link
**Params:** string $link, string $feed, string $type
**Since:** 2.5 | **Tags:** #Legacy
Filters the search feed link.

### tag_escape
**Params:** string $safe_tag, string $tag_name
**Since:** 2.5 | **Tags:** #Legacy
Filters a string cleaned and escaped for output as an HTML tag.

### term_link
**Params:** string $termlink, WP_Term $term, string $taxonomy
**Since:** 2.5 | **Tags:** #Legacy
Filters the term link.

### term_links-{$taxonomy}
**Since:** 2.5 | **Tags:** #Variable #Legacy

### term_name
**Params:** string $pad_tag_name, WP_Term $tag
**Since:** 2.5 | **Tags:** #Legacy
Filters display of the term name in the terms list table. The default output may include padding due to the term's current level in the term hierarchy.

### the_content_export
**Params:** string $post_content
**Since:** 2.5 | **Tags:** #Legacy
Filters the post content used for WXR exports.

### update_feedback
**Params:** string $feedback
**Since:** 2.5 | **Tags:** #Legacy
Filters feedback messages displayed during the core update process. The filter is first evaluated after the zip file for the latest version has been downloaded and unzipped. It is evaluated five more times during the process: 1. Before WordPress begins the core upgrade process. 2. Before Maintenance Mode is enabled. 3. Before WordPress begins copying over the necessary files. 4. Before Maintenance Mode is disabled. 5. Before the database is upgraded.

### wp_list_bookmarks
**Params:** string $html
**Since:** 2.5 | **Tags:** #Legacy
Filters the bookmarks list before it is echoed or returned.

### {$taxonomy}_{$field}_rss
**Since:** 2.5 | **Tags:** #Variable #Legacy

### get_archives_link
**Params:** string $link_html, string $url, string $text, string $format, string $before, string $after, bool $selected
**Since:** 2.6 | **Tags:** #Legacy
Filters the archive link content.

### get_post_time
**Params:** string|int $time, string $format, bool $gmt
**Since:** 2.6 | **Tags:** #Legacy
Filters the localized time of the post.

### the_excerpt_export
**Params:** string $post_excerpt
**Since:** 2.6 | **Tags:** #Legacy
Filters the post excerpt used for WXR exports.

### _wp_post_revision_fields
**Params:** string[] $fields, array $post
**Since:** 2.6 | **Tags:** #Legacy
Filters the list of fields saved in post revisions. Included by default: 'post_title', 'post_content' and 'post_excerpt'. Disallowed fields: 'ID', 'post_name', 'post_parent', 'post_date', 'post_date_gmt', 'post_status', 'post_type', 'comment_count', and 'post_author'.

### _wp_post_revision_field_{$field}
**Since:** 2.6 | **Tags:** #Variable #Legacy

### {$adjacent}_post_link
**Since:** 2.6 | **Tags:** #Variable #Legacy

### date_formats
**Params:** string[] $default_date_formats
**Since:** 2.7 | **Tags:** #Legacy
Filters the default date formats.

### edit_bookmark_link
**Params:** string $link, int $link_id
**Since:** 2.7 | **Tags:** #Legacy
Filters the bookmark edit link anchor tag.

### edit_tag_link
**Params:** string $link
**Since:** 2.7 | **Tags:** #Legacy
Filters the anchor tag for the edit link for a tag (or term in another taxonomy).

### excerpt_length
**Params:** int $number
**Since:** 2.7 | **Tags:** #Legacy
Filters the maximum number of words in a post excerpt.

### get_categories_taxonomy
**Since:** 2.7 | **Tags:** #Legacy

### get_comments_pagenum_link
**Params:** string $result
**Since:** 2.7 | **Tags:** #Legacy
Filters the comments page number link for the current request.

### get_edit_bookmark_link
**Params:** string $location, int $link_id
**Since:** 2.7 | **Tags:** #Legacy
Filters the bookmark edit link.

### get_edit_tag_link
**Params:** string $link
**Since:** 2.7 | **Tags:** #Legacy
Filters the edit link for a tag (or term in another taxonomy).

### get_search_form
**Params:** string $form, array $args
**Since:** 2.7 | **Tags:** #Legacy
Filters the HTML output of the search form.

### next_comments_link_attributes
**Params:** string $attributes
**Since:** 2.7 | **Tags:** #Legacy
Filters the anchor tag attributes for the next comments page link.

### next_posts_link_attributes
**Params:** string $attributes
**Since:** 2.7 | **Tags:** #Legacy
Filters the anchor tag attributes for the next posts page link.

### post_class
**Params:** string[] $classes, string[] $css_class, int $post_id
**Since:** 2.7 | **Tags:** #Legacy
Filters the list of CSS class names for the current post.

### post_comments_link
**Params:** string $post_reply_link, int|WP_Post $post
**Since:** 2.7 | **Tags:** #Legacy
Filters the formatted post comments link HTML.

### previous_comments_link_attributes
**Params:** string $attributes
**Since:** 2.7 | **Tags:** #Legacy
Filters the anchor tag attributes for the previous comments page link.

### previous_posts_link_attributes
**Params:** string $attributes
**Since:** 2.7 | **Tags:** #Legacy
Filters the anchor tag attributes for the previous posts page link.

### rss_update_frequency
**Params:** string $frequency
**Since:** 2.7 | **Tags:** #Legacy
Filters the RSS update frequency.

### rss_update_period
**Params:** string $duration
**Since:** 2.7 | **Tags:** #Legacy
Filters how often to update the RSS feed.

### the_password_form
**Params:** string $output, WP_Post $post, string $invalid_password
**Since:** 2.7 | **Tags:** #Legacy
Filters the HTML output for the protected post password form. If modifying the password field, please note that the WordPress database schema limits the password field to 255 characters regardless of the value of the `minlength` or `maxlength` attributes or other validation that may be added to the input.

### the_preview
**Since:** 2.7 | **Tags:** #Legacy

### time_formats
**Params:** string[] $default_time_formats
**Since:** 2.7 | **Tags:** #Legacy
Filters the default time formats.

### wp_insert_post_data
**Params:** array $data, array $postarr, array $unsanitized_postarr, bool $update
**Since:** 2.7 | **Tags:** #Legacy
Filters slashed post data just before it is inserted into the database.

### wp_page_menu
**Params:** string $menu, array $args
**Since:** 2.7 | **Tags:** #Legacy
Filters the HTML output of a page-based menu.

### wp_page_menu_args
**Params:** array $args
**Since:** 2.7 | **Tags:** #Legacy
Filters the arguments used to generate a page-based menu.

### body_class
**Params:** string[] $classes, string[] $css_class
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of CSS body class names for the current post or page.

### content_url
**Params:** string $url, string $path
**Since:** 2.8 | **Tags:** #Legacy
Filters the URL to the content directory.

### date_i18n
**Params:** string $date, string $format, int $timestamp, bool $gmt
**Since:** 2.8 | **Tags:** #Legacy
Filters the date formatted based on the locale.

### get_post_modified_time
**Params:** string|int $time, string $format, bool $gmt
**Since:** 2.8 | **Tags:** #Legacy
Filters the localized time a post was last modified.

### get_terms_fields
**Since:** 2.8 | **Tags:** #Legacy

### get_terms_orderby
**Params:** string $orderby, array $args, string[] $taxonomies
**Since:** 2.8 | **Tags:** #Legacy
Filters the ORDERBY clause of the terms query.

### iis7_url_rewrite_rules
**Params:** string $rules
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of rewrite rules formatted for output to a web.config.

### index_rel_link
**Since:** 2.8 | **Tags:** #Legacy

### number_format_i18n
**Params:** string $formatted, float $number, int $decimals
**Since:** 2.8 | **Tags:** #Legacy
Filters the number formatted based on the locale.

### page_css_class
**Since:** 2.8 | **Tags:** #Legacy

### parent_post_rel_link
**Since:** 2.8 | **Tags:** #Legacy

### post_comments_feed_link_html
**Params:** string $link, int $post_id, string $feed
**Since:** 2.8 | **Tags:** #Legacy
Filters the post comment feed link anchor tag.

### private_title_format
**Params:** string $prepend, WP_Post $post
**Since:** 2.8 | **Tags:** #Legacy
Filters the text prepended to the post title of private posts. The filter is only applied on the front end.

### protected_title_format
**Params:** string $prepend, WP_Post $post
**Since:** 2.8 | **Tags:** #Legacy
Filters the text prepended to the post title for protected posts. The filter is only applied on the front end.

### tag_cloud_sort
**Params:** WP_Term[] $tags, array $args
**Since:** 2.8 | **Tags:** #Legacy
Filters how the items in a tag cloud are sorted.

### terms_to_edit
**Params:** string $terms_to_edit, string $taxonomy
**Since:** 2.8 | **Tags:** #Legacy
Filters the comma-separated list of terms available to edit.

### the_content_more_link
**Params:** string $more_link_element, string $more_link_text
**Since:** 2.8 | **Tags:** #Legacy
Filters the Read More link text.

### wp_get_object_terms
**Params:** WP_Term[]|int[]|string[]|string $terms, string $object_ids, string $taxonomies, array $args
**Since:** 2.8 | **Tags:** #Legacy
Filters the terms for a given object or objects. The `$taxonomies` parameter passed to this filter is formatted as a SQL fragment. The {@see 'get_object_terms'} filter is recommended as an alternative.

### wp_trim_excerpt
**Params:** string $text, string $raw_excerpt
**Since:** 2.8 | **Tags:** #Legacy
Filters the trimmed excerpt string.

### {$adjacent}_post_rel_link
**Since:** 2.8 | **Tags:** #Variable #Legacy

### {$boundary}_post_rel_link
**Since:** 2.8 | **Tags:** #Variable #Legacy

### excerpt_more
**Params:** string $more_string
**Since:** 2.9 | **Tags:** #Legacy
Filters the string in the "more" link displayed after a trimmed excerpt.

### get_delete_post_link
**Params:** string $link, int $post_id, bool $force_delete
**Since:** 2.9 | **Tags:** #Legacy
Filters the post delete link.

### get_sample_permalink_html
**Params:** string $return, int $post_id, string|null $new_title, string|null $new_slug, WP_Post $post
**Since:** 2.9 | **Tags:** #Legacy
Filters the sample permalink HTML markup.

### redirect_post_location
**Params:** string $location, int $post_id
**Since:** 2.9 | **Tags:** #Legacy
Filters the post redirect destination URL.

### the_content_feed
**Params:** string $content, string $feed_type
**Since:** 2.9 | **Tags:** #Legacy
Filters the post content for use in feeds.

### the_terms
**Params:** string $term_list, string $taxonomy, string $before, string $sep, string $after
**Since:** 2.9 | **Tags:** #Legacy
Filters the list of terms to display.

### get_calendar
**Params:** string $calendar_output, array $args
**Since:** 3.0 | **Tags:** #Modern
Filters the HTML calendar output.

### get_shortlink
**Params:** string $shortlink, int $id, string $context, bool $allow_slugs
**Since:** 3.0 | **Tags:** #Modern
Filters the shortlink for a post.

### get_the_date
**Params:** string|int $the_date, string $format, WP_Post $post
**Since:** 3.0 | **Tags:** #Modern
Filters the date of the post.

### nav_menu_attr_title
**Params:** string $item_title
**Since:** 3.0 | **Tags:** #Modern
Filters a navigation menu item's title attribute.

### nav_menu_css_class
**Since:** 3.0 | **Tags:** #Modern

### nav_menu_description
**Params:** string $description
**Since:** 3.0 | **Tags:** #Modern
Filters a navigation menu item's description.

### nav_menu_meta_box_object
**Params:** WP_Post_Type|false $post_type
**Since:** 3.0 | **Tags:** #Modern
Filters whether a menu items meta box will be added for the current object type. If a falsey value is returned instead of an object, the menu items meta box for the current meta box object will not be added.

### posts_search
**Since:** 3.0 | **Tags:** #Modern

### post_type_link
**Params:** string $post_link, WP_Post $post, bool $leavename, bool $sample
**Since:** 3.0 | **Tags:** #Modern
Filters the permalink for a post of a custom post type.

### pre_get_shortlink
**Params:** false|string $return, int $id, string $context, bool $allow_slugs
**Since:** 3.0 | **Tags:** #Modern
Filters whether to preempt generating a shortlink for the given post. Returning a value other than false from the filter will short-circuit the shortlink generation process, returning that value instead.

### pre_insert_term
**Params:** string|WP_Error $term, string $taxonomy, array|string $args
**Since:** 3.0 | **Tags:** #Modern
Filters a term before it is sanitized and inserted into the database.

### pre_post_link
**Params:** string $permalink, WP_Post $post, bool $leavename
**Since:** 3.0 | **Tags:** #Modern
Filters the permalink structure for a post before token replacement occurs. Only applies to posts with post_type of 'post'.

### search_link
**Params:** string $link, string $search
**Since:** 3.0 | **Tags:** #Modern
Filters the search permalink.

### taxonomy_feed_link
**Params:** string $link, string $feed, string $taxonomy
**Since:** 3.0 | **Tags:** #Modern
Filters the feed link for a taxonomy other than 'category' or 'post_tag'.

### the_feed_link
**Params:** string $link, string $feed
**Since:** 3.0 | **Tags:** #Modern
Filters the feed link anchor tag.

### the_shortlink
**Params:** string $link, string $shortlink, string $text, string $title
**Since:** 3.0 | **Tags:** #Modern
Filters the short link anchor tag for a post.

### walker_nav_menu_start_el
**Params:** string $item_output, WP_Post $menu_item, int $depth, stdClass $args
**Since:** 3.0 | **Tags:** #Modern
Filters a menu item's starting output. The menu item's starting output only includes `$args->before`, the opening `<a>`, the menu item's title, the closing `</a>`, and `$args->after`. Currently, there is no filter for modifying the opening and closing `<li>` for a menu item.

### wp_edit_nav_menu_walker
**Params:** string $class, int $menu_id
**Since:** 3.0 | **Tags:** #Modern
Filters the Walker class used when adding nav menu items.

### wp_get_nav_menus
**Params:** WP_Term[] $menus, array $args
**Since:** 3.0 | **Tags:** #Modern
Filters the navigation menu objects being returned.

### wp_get_nav_menu_items
**Params:** array $items, object $menu, array $args
**Since:** 3.0 | **Tags:** #Modern
Filters the navigation menu items being returned.

### wp_link_pages_args
**Params:** array $parsed_args
**Since:** 3.0 | **Tags:** #Modern
Filters the arguments used in retrieving page links for paginated posts.

### wp_nav_menu
**Params:** string $nav_menu, stdClass $args
**Since:** 3.0 | **Tags:** #Modern
Filters the HTML content for navigation menus.

### wp_nav_menu_args
**Params:** array $args
**Since:** 3.0 | **Tags:** #Modern
Filters the arguments used to display a navigation menu.

### wp_nav_menu_container_allowedtags
**Params:** string[] $tags
**Since:** 3.0 | **Tags:** #Modern
Filters the list of HTML tags that are valid for use as menu containers.

### wp_nav_menu_items
**Params:** string $items, stdClass $args
**Since:** 3.0 | **Tags:** #Modern
Filters the HTML list content for navigation menus.

### wp_nav_menu_{$menu->slug}_items
**Since:** 3.0 | **Tags:** #Variable #Modern

### wp_setup_nav_menu_item
**Params:** object $menu_item
**Since:** 3.0 | **Tags:** #Modern
Filters a navigation menu item object.

### {$taxonomy}_row_actions
**Since:** 3.0 | **Tags:** #Variable #Modern

### {$type}_upload_iframe_src
**Since:** 3.0 | **Tags:** #Variable #Modern

### edit_term_link
**Params:** string $link, int $term_id
**Since:** 3.1 | **Tags:** #Modern
Filters the anchor tag for the edit link of a term.

### get_ancestors
**Params:** int[] $ancestors, int $object_id, string $object_type, string $resource_type
**Since:** 3.1 | **Tags:** #Modern
Filters a given object's ancestors.

### get_edit_term_link
**Params:** string $location, int $term_id, string $taxonomy, string $object_type
**Since:** 3.1 | **Tags:** #Modern
Filters the edit link for a term.

### get_meta_sql
**Since:** 3.1 | **Tags:** #Modern

### get_terms_args
**Params:** array $args, string[] $taxonomies
**Since:** 3.1 | **Tags:** #Modern
Filters the terms query arguments.

### get_the_categories
**Params:** WP_Term[] $categories, int|false $post_id
**Since:** 3.1 | **Tags:** #Modern
Filters the array of categories to return for a post.

### get_the_terms
**Params:** WP_Term[]|WP_Error $terms, int $post_id, string $taxonomy
**Since:** 3.1 | **Tags:** #Modern
Filters the list of terms attached to the given post.

### list_pages
**Params:** string $title, WP_Post $page
**Since:** 3.1 | **Tags:** #Modern
Filters the page title when creating an HTML drop-down list of pages.

### nav_menu_item_id
**Params:** string $menu_item_id, WP_Post $menu_item, stdClass $args, int $depth
**Since:** 3.1 | **Tags:** #Modern
Filters the ID attribute applied to a menu item's list item element.

### posts_clauses
**Since:** 3.1 | **Tags:** #Modern

### posts_clauses_request
**Since:** 3.1 | **Tags:** #Modern

### post_format_rewrite_base
**Params:** string $context
**Since:** 3.1 | **Tags:** #Modern
Filters the post formats rewrite base.

### post_type_archive_feed_link
**Params:** string $link, string $feed
**Since:** 3.1 | **Tags:** #Modern
Filters the post type archive feed link.

### post_type_archive_link
**Params:** string $link, string $post_type
**Since:** 3.1 | **Tags:** #Modern
Filters the post type archive permalink.

### post_type_archive_title
**Params:** string $post_type_name, string $post_type
**Since:** 3.1 | **Tags:** #Modern
Filters the post type archive title.

### single_term_title
**Params:** string $term_name
**Since:** 3.1 | **Tags:** #Modern
Filters the custom taxonomy archive page title.

### terms_clauses
**Params:** string[] $clauses, string[] $taxonomies, array $args
**Since:** 3.1 | **Tags:** #Modern
Filters the terms query SQL clauses.

### wp_insert_post_parent
**Params:** int $post_parent, int $post_id, array $new_postarr, array $postarr
**Since:** 3.1 | **Tags:** #Modern
Filters the post parent -- used to check for and prevent hierarchy loops.

### wp_nav_menu_objects
**Params:** array $sorted_menu_items, stdClass $args
**Since:** 3.1 | **Tags:** #Modern
Filters the sorted list of menu item objects before generating the menu's HTML.

### wp_unique_post_slug_is_bad_attachment_slug
**Params:** bool $bad_slug, string $slug
**Since:** 3.1 | **Tags:** #Modern
Filters whether the post slug would make a bad attachment slug.

### wp_unique_post_slug_is_bad_flat_slug
**Params:** bool $bad_slug, string $slug, string $post_type
**Since:** 3.1 | **Tags:** #Modern
Filters whether the post slug would be bad as a flat slug.

### wp_unique_post_slug_is_bad_hierarchical_slug
**Params:** bool $bad_slug, string $slug, string $post_type, int $post_parent
**Since:** 3.1 | **Tags:** #Modern
Filters whether the post slug would make a bad hierarchical post slug.

### wp_update_term_parent
**Params:** int $parent_term, int $term_id, string $taxonomy, array $parsed_args, array $args
**Since:** 3.1 | **Tags:** #Modern
Filters the term parent. Hook to this filter to see if it will cause a hierarchy loop.

### {$permastructname}_rewrite_rules
**Since:** 3.1 | **Tags:** #Variable #Modern

### nav_menu_items_{$post_type_name}
**Since:** 3.2 | **Tags:** #Variable #Modern

### wp_insert_post_empty_content
**Params:** bool $maybe_empty, array $postarr
**Since:** 3.3 | **Tags:** #Modern
Filters whether the post should be considered "empty". The post is considered "empty" if both: 1. The post type supports the title, editor, and excerpt fields 2. The title, editor, and excerpt fields are all empty Returning a truthy value from the filter will effectively short-circuit the new post being inserted and return 0. If $wp_error is true, a WP_Error will be returned instead.

### wp_trim_words
**Params:** string $text, int $num_words, string $more, string $original_text
**Since:** 3.3 | **Tags:** #Modern
Filters the text content after words have been trimmed.

### wp_unique_post_slug
**Params:** string $slug, int $post_id, string $post_status, string $post_type, int $post_parent, string $original_slug
**Since:** 3.3 | **Tags:** #Modern
Filters the unique post slug.

### wxr_export_skip_postmeta
**Params:** bool $skip, string $meta_key, object $meta
**Since:** 3.3 | **Tags:** #Modern
Filters whether to selectively skip post meta used for WXR exports. Returning a truthy value from the filter will skip the current meta object from being exported.

### {$type}_send_to_editor_url
**Since:** 3.3 | **Tags:** #Variable #Modern

### posts_request_ids
**Params:** string $request, WP_Query $query
**Since:** 3.4 | **Tags:** #Modern
Filters the Post IDs SQL request before sending.

### post_types_to_delete_with_user
**Params:** string[] $post_types_to_delete, int $id
**Since:** 3.4 | **Tags:** #Modern
Filters the list of post types to delete with a user.

### export_args
**Params:** array $args
**Since:** 3.5 | **Tags:** #Modern
Filters the export args.

### post_link_category
**Params:** WP_Term $cat, array $cats, WP_Post $post
**Since:** 3.5 | **Tags:** #Modern
Filters the category that gets used in the %category% permalink token.

### post_type_labels_{$post_type}
**Since:** 3.5 | **Tags:** #Variable #Modern

### wp_checkdate
**Params:** bool $checkdate, string $source_date
**Since:** 3.5 | **Tags:** #Modern
Filters whether the given date is valid for the Gregorian calendar.

### {$adjacent}_image_link
**Since:** 3.5 | **Tags:** #Variable #Modern

### get_comments_link
**Params:** string $comments_link, int|WP_Post $post
**Since:** 3.6 | **Tags:** #Modern
Filters the returned post comments permalink.

### get_post_galleries
**Params:** array $galleries, WP_Post $post
**Since:** 3.6 | **Tags:** #Modern
Filters the list of all found galleries in the given post.

### get_post_gallery
**Params:** array $gallery, int|WP_Post $post, array $galleries
**Since:** 3.6 | **Tags:** #Modern
Filters the first-found post gallery.

### nav_menu_link_attributes
**Params:** array $atts, WP_Post $menu_item, stdClass $args, int $depth
**Since:** 3.6 | **Tags:** #Modern
Filters the HTML attributes applied to a menu item's anchor element.

### search_form_format
**Params:** string $format, array $args
**Since:** 3.6 | **Tags:** #Modern
Filters the HTML format of the search form.

### self_link
**Params:** string $feed_link
**Since:** 3.6 | **Tags:** #Modern
Filters the current feed URL.

### wp_link_pages
**Params:** string $output, array|string $args
**Since:** 3.6 | **Tags:** #Modern
Filters the HTML output of page links for paginated posts.

### wp_link_pages_link
**Params:** string $link, int $i
**Since:** 3.6 | **Tags:** #Modern
Filters the HTML output of individual page number links.

### posts_search_orderby
**Params:** string $search_orderby, WP_Query $query
**Since:** 3.7 | **Tags:** #Modern
Filters the ORDER BY used when ordering search results.

### post_password_expires
**Params:** int $expires
**Since:** 3.7 | **Tags:** #Modern
Filters the life span of the post password cookie. By default, the cookie expires 10 days from creation. To turn this into a session cookie, return 0.

### taxonomy_parent_dropdown_args
**Params:** array $dropdown_args, string $taxonomy, string $context
**Since:** 3.7 | **Tags:** #Modern
Filters the taxonomy parent drop-down on the Edit Term page.

### term_updated_messages
**Params:** array[] $messages
**Since:** 3.7 | **Tags:** #Modern
Filters the messages displayed when a tag is updated.

### post_playlist
**Params:** string $output, array $attr, int $instance
**Since:** 3.9 | **Tags:** #Modern
Filters the playlist output. Returning a non-empty value from the filter will short-circuit generation of the default playlist output, returning the passed value instead.

### pre_wp_nav_menu
**Params:** string|null $output, stdClass $args
**Since:** 3.9 | **Tags:** #Modern
Filters whether to short-circuit the wp_nav_menu() output. Returning a non-null value from the filter will short-circuit wp_nav_menu(), echoing that value if $args->echo is true, returning that value otherwise.

### edit_{$post_type}_per_page
**Since:** 4.0 | **Tags:** #Variable #Modern

### term_search_min_chars
**Params:** int $characters, WP_Taxonomy $taxonomy_object, string $search
**Since:** 4.0 | **Tags:** #Modern
Filters the minimum number of characters required to fire a tag search via Ajax.

### wp_list_comments_args
**Params:** array $parsed_args
**Since:** 4.0 | **Tags:** #Modern
Filters the arguments used in retrieving the comment list.

### wp_title_parts
**Params:** string[] $title_array
**Since:** 4.0 | **Tags:** #Modern
Filters the parts of the page title.

### wxr_export_skip_commentmeta
**Params:** bool $skip, string $meta_key, object $meta
**Since:** 4.0 | **Tags:** #Modern
Filters whether to selectively skip comment meta used for WXR exports. Returning a truthy value from the filter will skip the current meta object from being exported.

### default_page_template_title
**Params:** string $label, string $context
**Since:** 4.1 | **Tags:** #Modern
Filters the title of the default page template displayed in the drop-down.

### get_the_archive_description
**Params:** string $description
**Since:** 4.1 | **Tags:** #Modern
Filters the archive description.

### get_the_archive_title
**Params:** string $title, string $original_title, string $prefix
**Since:** 4.1 | **Tags:** #Modern
Filters the archive title.

### category_css_class
**Since:** 4.2 | **Tags:** #Modern

### get_object_terms
**Params:** WP_Term[]|int[]|string[]|string $terms, int[] $object_ids, string[] $taxonomies, array $args
**Since:** 4.2 | **Tags:** #Modern
Filters the terms for a given object or objects.

### the_guid
**Params:** string $post_guid, int $post_id
**Since:** 4.2 | **Tags:** #Modern
Filters the escaped Global Unique Identifier (guid) of the post.

### edit_comment_misc_actions
**Params:** string $html, WP_Comment $comment
**Since:** 4.3 | **Tags:** #Modern
Filters miscellaneous actions for the edit comment form sidebar.

### get_default_comment_status
**Params:** string $status, string $post_type, string $comment_type
**Since:** 4.3 | **Tags:** #Modern
Filters the default comment status for the given post type.

### has_nav_menu
**Params:** bool $has_nav_menu, string $location
**Since:** 4.3 | **Tags:** #Modern
Filters whether a nav menu is assigned to the specified location.

### nav_menu_items_{$post_type_name}_recent
**Since:** 4.3 | **Tags:** #Variable #Modern

### wp_generate_tag_cloud_data
**Params:** array[] $tags_data
**Since:** 4.3 | **Tags:** #Modern
Filters the data used to generate the tag cloud.

### wp_get_nav_menu_object
**Params:** WP_Term|false $menu_obj, int|string|WP_Term $menu
**Since:** 4.3 | **Tags:** #Modern
Filters the nav_menu term retrieved for wp_get_nav_menu_object().

### content_pagination
**Params:** string[] $pages, WP_Post $post
**Since:** 4.4 | **Tags:** #Modern
Filters the "pages" derived from splitting the post content. "Pages" are determined by splitting the post content based on the presence of `<!-- nextpage -->` tags.

### document_title_parts
**Params:** array $title
**Since:** 4.4 | **Tags:** #Modern
Filters the parts of the document title.

### document_title_separator
**Params:** string $sep
**Since:** 4.4 | **Tags:** #Modern
Filters the separator for the document title.

### duplicate_comment_id
**Params:** int $dupe_id, array $commentdata
**Since:** 4.4 | **Tags:** #Modern
Filters the ID, if any, of the duplicate comment found when creating a new comment. Return an empty value from this filter to allow what WP considers a duplicate comment.

### enclosure_links
**Params:** string[] $post_links, int $post_id
**Since:** 4.4 | **Tags:** #Modern
Filters the list of enclosure links before querying the database. Allows for the addition and/or removal of potential enclosures to save to postmeta before checking the database for existing enclosures.

### export_wp_filename
**Params:** string $wp_filename, string $sitename, string $date
**Since:** 4.4 | **Tags:** #Modern
Filters the export filename.

### feed_links_show_comments_feed
**Params:** bool $show
**Since:** 4.4 | **Tags:** #Modern
Filters whether to display the comments feed link.

### feed_links_show_posts_feed
**Params:** bool $show
**Since:** 4.4 | **Tags:** #Modern
Filters whether to display the posts feed link.

### get_page_of_comment
**Params:** int $page, array $args, array $original_args, int $comment_id
**Since:** 4.4 | **Tags:** #Modern
Filters the calculated page on which a comment appears.

### get_page_uri
**Params:** string $uri, WP_Post $page
**Since:** 4.4 | **Tags:** #Modern
Filters the URI for a page.

### get_post_status
**Params:** string $post_status, WP_Post $post
**Since:** 4.4 | **Tags:** #Modern
Filters the post status.

### get_sample_permalink
**Params:** array $permalink, int $post_id, string $title, string $name, WP_Post $post
**Since:** 4.4 | **Tags:** #Modern
Filters the sample permalink.

### get_terms_defaults
**Params:** array $defaults, string[] $taxonomies
**Since:** 4.4 | **Tags:** #Modern
Filters the terms query default arguments. Use {@see 'get_terms_args'} to filter the passed arguments.

### get_{$adjacent}_post_excluded_terms
**Since:** 4.4 | **Tags:** #Variable #Modern

### nav_menu_item_args
**Params:** stdClass $args, WP_Post $menu_item, int $depth
**Since:** 4.4 | **Tags:** #Modern
Filters the arguments for a single nav menu item.

### nav_menu_item_title
**Params:** string $title, WP_Post $menu_item, stdClass $args, int $depth
**Since:** 4.4 | **Tags:** #Modern
Filters a menu item's title.

### notify_moderator
**Params:** bool $maybe_notify, int $comment_id
**Since:** 4.4 | **Tags:** #Modern
Filters whether to send the site moderator email notifications, overriding the site setting.

### notify_post_author
**Params:** bool $maybe_notify, int $comment_id
**Since:** 4.4 | **Tags:** #Modern
Filters whether to send the post author new comment notification emails, overriding the site setting.

### old_slug_redirect_url
**Params:** string $link
**Since:** 4.4 | **Tags:** #Modern
Filters the old slug redirect URL.

### postmeta_form_keys
**Params:** array|null $keys, WP_Post $post
**Since:** 4.4 | **Tags:** #Modern
Filters values for the meta key dropdown in the Custom Fields meta box. Returning a non-null value will effectively short-circuit and avoid a potentially expensive query against postmeta.

### post_edit_category_parent_dropdown_args
**Params:** array $parent_dropdown_args
**Since:** 4.4 | **Tags:** #Modern
Filters the arguments for the taxonomy parent dropdown on the Post Edit page.

### post_embed_url
**Params:** string $embed_url, WP_Post $post
**Since:** 4.4 | **Tags:** #Modern
Filters the URL to embed a specific post.

### pre_delete_post
**Params:** WP_Post|false|null $check, WP_Post $post, bool $force_delete
**Since:** 4.4 | **Tags:** #Modern
Filters whether a post deletion should take place.

### pre_get_document_title
**Params:** string $title
**Since:** 4.4 | **Tags:** #Modern
Filters the document title before it is generated. Passing a non-empty value will short-circuit wp_get_document_title(), returning that value instead.

### pre_get_lastpostmodified
**Params:** string|false $lastpostmodified, string $timezone, string $post_type
**Since:** 4.4 | **Tags:** #Modern
Pre-filter the return value of get_lastpostmodified() before the query is run.

### respond_link
**Params:** string $respond_link, int $post_id
**Since:** 4.4 | **Tags:** #Modern
Filters the respond link when a post has no comments.

### taxonomy_labels_{$taxonomy}
**Since:** 4.4 | **Tags:** #Variable #Modern

### the_category_list
**Params:** WP_Term[] $categories, int|false $post_id
**Since:** 4.4 | **Tags:** #Modern
Filters the categories before building the category list.

### the_excerpt_embed
**Params:** string $output
**Since:** 4.4 | **Tags:** #Modern
Filters the post excerpt for the embed template.

### wp_dropdown_users_args
**Params:** array $query_args, array $parsed_args
**Since:** 4.4 | **Tags:** #Modern
Filters the query arguments for the list of users in the dropdown.

### get_custom_logo
**Params:** string $html, int $blog_id
**Since:** 4.5 | **Tags:** #Modern
Filters the custom logo output.

### pre_handle_404
**Params:** bool $preempt, WP_Query $wp_query
**Since:** 4.5 | **Tags:** #Modern
Filters whether to short-circuit default header status handling. Returning a non-false value from the filter will short-circuit the handling and return early.

### pre_wp_update_comment_count_now
**Params:** int|null $new, int $old, int $post_id
**Since:** 4.5 | **Tags:** #Modern
Filters a post's comment count before it is updated in the database.

### get_canonical_url
**Params:** string $canonical_url, WP_Post $post
**Since:** 4.6 | **Tags:** #Modern
Filters the canonical URL for a post.

### posts_pre_query
**Since:** 4.6 | **Tags:** #Modern

### redirect_term_location
**Params:** string $location, WP_Taxonomy $tax
**Since:** 4.6 | **Tags:** #Modern
Filters the taxonomy redirect destination URL.

### the_post_thumbnail_caption
**Params:** string $caption
**Since:** 4.6 | **Tags:** #Modern
Filters the displayed post thumbnail caption.

### wxr_export_skip_termmeta
**Params:** bool $skip, string $meta_key, object $meta
**Since:** 4.6 | **Tags:** #Modern
Filters whether to selectively skip term meta used for WXR exports. Returning a truthy value from the filter will skip the current meta object from being exported.

### post_password_required
**Params:** bool $required, WP_Post $post
**Since:** 4.7 | **Tags:** #Modern
Filters whether a post requires the user to supply a password.

### wp_update_term_data
**Params:** array $data, int $term_id, string $taxonomy, array $args
**Since:** 4.7 | **Tags:** #Modern
Filters term data before it is updated in the database.

### nav_menu_submenu_css_class
**Since:** 4.8 | **Tags:** #Modern

### post_date_column_status
**Params:** string $status, WP_Post $post, string $column_name, string $mode
**Since:** 4.8 | **Tags:** #Modern
Filters the status text of the post.

### get_the_post_type_description
**Params:** string $description, WP_Post_Type $post_type_obj
**Since:** 4.9 | **Tags:** #Modern
Filters the description for a post type archive.

### pre_term_link
**Params:** string $termlink, WP_Term $term
**Since:** 4.9 | **Tags:** #Modern
Filters the permalink structure for a term before token replacement occurs.

### pre_trash_post
**Params:** bool|null $trash, WP_Post $post, string $previous_status
**Since:** 4.9 | **Tags:** #Modern
Filters whether a post trashing should take place.

### pre_untrash_post
**Params:** bool|null $untrash, WP_Post $post, string $previous_status
**Since:** 4.9 | **Tags:** #Modern
Filters whether a post untrashing should take place.

### replace_editor
**Params:** bool $replace, WP_Post $post
**Since:** 4.9 | **Tags:** #Modern
Allows replacement of the editor.

### wp_get_nav_menu_name
**Params:** string $menu_name, string $location
**Since:** 4.9 | **Tags:** #Modern
Filters the navigation menu name being returned.

### wp_get_object_terms_args
**Params:** array $args, int[] $object_ids, string[] $taxonomies
**Since:** 4.9 | **Tags:** #Modern
Filters arguments for retrieving object terms.

### excerpt_allowed_blocks
**Params:** string[] $allowed_blocks
**Since:** 5.0 | **Tags:** #Recent
Filters the list of blocks that can contribute to the excerpt. If a dynamic block is added to this list, it must not generate another excerpt, as this will cause an infinite loop to occur.

### filter_block_editor_meta_boxes
**Params:** array $wp_meta_boxes
**Since:** 5.0 | **Tags:** #Recent
Fires right before the meta boxes are rendered. This allows for the filtering of meta box data, that should already be present by this point. Do not use as a means of adding meta box data.

### old_slug_redirect_post_id
**Params:** int $id
**Since:** 5.0 | **Tags:** #Recent
Filters the old slug redirect post ID.

### privacy_policy_url
**Params:** string $url, int $policy_page_id
**Since:** 5.0 | **Tags:** #Recent
Filters the URL of the privacy policy page.

### render_block
**Params:** string $block_content, array $block, WP_Block $instance
**Since:** 5.0 | **Tags:** #Recent
Filters the content of a single block.

### the_privacy_policy_link
**Params:** string $link, string $privacy_policy_url
**Since:** 5.0 | **Tags:** #Recent
Filters the privacy policy link.

### use_block_editor_for_post
**Params:** bool $use_block_editor, WP_Post $post
**Since:** 5.0 | **Tags:** #Recent
Filters whether a post is able to be edited in the block editor.

### use_block_editor_for_post_type
**Params:** bool $use_block_editor, string $post_type
**Since:** 5.0 | **Tags:** #Recent
Filters whether a post is able to be edited in the block editor.

### allow_empty_comment
**Params:** bool $allow_empty_comment, array $commentdata
**Since:** 5.1 | **Tags:** #Recent
Filters whether an empty comment should be allowed.

### block_editor_no_javascript_message
**Params:** string $message, WP_Post $post, bool $installed
**Since:** 5.1 | **Tags:** #Recent
Filters the message displayed in the block editor interface when JavaScript is not enabled in the browser.

### has_post_thumbnail
**Params:** bool $has_thumbnail, int|WP_Post|null $post, int|false $thumbnail_id
**Since:** 5.1 | **Tags:** #Recent
Filters whether a post has a post thumbnail.

### pre_render_block
**Params:** string|null $pre_render, array $parsed_block, WP_Block|null $parent_block
**Since:** 5.1 | **Tags:** #Recent
Allows render_block() to be short-circuited, by returning a non-null value.

### pre_wp_unique_post_slug
**Params:** string|null $override_slug, string $slug, int $post_id, string $post_status, string $post_type, int $post_parent
**Since:** 5.1 | **Tags:** #Recent
Filters the post slug before it is generated to be unique. Returning a non-null value will short-circuit the unique slug generation, returning the passed value instead.

### render_block_data
**Params:** array $parsed_block, array $source_block, WP_Block|null $parent_block
**Since:** 5.1 | **Tags:** #Recent
Filters the block being rendered in render_block(), before it's processed.

### category_list_link_attributes
**Params:** array $atts, WP_Term $category, int $depth, array $args, int $current_object_id
**Since:** 5.2 | **Tags:** #Recent
Filters the HTML attributes applied to a category list item's anchor element.

### get_feed_build_date
**Params:** string|false $max_modified_time, string $format
**Since:** 5.2 | **Tags:** #Recent
Filters the date the last post or comment in the query was modified.

### post_column_taxonomy_links
**Params:** string[] $term_links, string $taxonomy, WP_Term[] $terms
**Since:** 5.2 | **Tags:** #Recent
Filters the links in `$taxonomy` column of edit.php.

### search_form_args
**Params:** array $args
**Since:** 5.2 | **Tags:** #Recent
Filters the array of arguments used when generating the search form.

### is_sticky
**Params:** bool $is_sticky, int $post_id
**Since:** 5.3 | **Tags:** #Recent
Filters whether a post is sticky.

### terms_pre_query
**Since:** 5.3 | **Tags:** #Recent

### add_trashed_suffix_to_trashed_posts
**Params:** bool $add_trashed_suffix, string $post_name, int $post_id
**Since:** 5.4 | **Tags:** #Recent
Filters whether or not to add a `__trashed` suffix to the name of trashed posts that match the name of the updated post.

### default_category_post_types
**Params:** string[] $post_types
**Since:** 5.5 | **Tags:** #Recent
Filters post types (in addition to 'post') that require a default category.

### do_redirect_guess_404_permalink
**Params:** bool $do_redirect_guess
**Since:** 5.5 | **Tags:** #Recent
Filters whether to attempt to guess a redirect URL for a 404 request. Returning a false value from the filter will disable the URL guessing and return early without performing a redirect.

### get_page_of_comment_query_args
**Params:** array $comment_args
**Since:** 5.5 | **Tags:** #Recent
Filters the arguments used to query comments in get_page_of_comment().

### get_the_archive_title_prefix
**Params:** string $prefix
**Since:** 5.5 | **Tags:** #Recent
Filters the archive title prefix.

### pre_redirect_guess_404_permalink
**Params:** null|string|false $pre
**Since:** 5.5 | **Tags:** #Recent
Short-circuits the redirect URL guessing for 404 requests. Returning a non-null value from the filter will effectively short-circuit the URL guessing, returning the passed value instead.

### render_block_context
**Params:** array $context, array $parsed_block, WP_Block|null $parent_block
**Since:** 5.5 | **Tags:** #Recent
Filters the default context provided to a rendered block.

### strict_redirect_guess_404_permalink
**Params:** bool $strict_guess
**Since:** 5.5 | **Tags:** #Recent
Filters whether to perform a strict guess for a 404 redirect. Returning a truthy value from the filter will redirect only exact post_name matches.

### block_default_classname
**Params:** string $class_name, string $block_name
**Since:** 5.6 | **Tags:** #Recent
Filters the default block className for server rendered blocks.

### should_load_block_editor_scripts_and_styles
**Params:** bool $is_block_editor_screen
**Since:** 5.6 | **Tags:** #Recent
Filters the flag that decides whether or not block editor scripts and styles are going to be enqueued on the current screen.

### block_type_metadata
**Params:** array $metadata
**Since:** 5.7 | **Tags:** #Recent
Filters the metadata provided for registering a block type.

### block_type_metadata_settings
**Params:** array $settings, array $metadata
**Since:** 5.7 | **Tags:** #Recent
Filters the settings determined from the block type metadata.

### render_block_{$this->name}
**Since:** 5.7 | **Tags:** #Variable #Recent

### the_title_export
**Params:** string $post_title
**Since:** 5.7 | **Tags:** #Recent
Filters the post title used for WXR exports.

### update_post_term_count_statuses
**Params:** string[] $post_statuses, WP_Taxonomy $taxonomy
**Since:** 5.7 | **Tags:** #Recent
Filters the post statuses for updating the term count.

### wp_list_table_show_post_checkbox
**Params:** bool $show, WP_Post $post
**Since:** 5.7 | **Tags:** #Recent
Filters whether to show the bulk edit checkbox for a post in its list table. By default the checkbox is only shown if the current user can edit the post.

### allowed_block_types_all
**Params:** bool|string[] $allowed_block_types, WP_Block_Editor_Context $block_editor_context
**Since:** 5.8 | **Tags:** #Recent
Filters the allowed block types for all editor types.

### block_categories_all
**Params:** array[] $block_categories, WP_Block_Editor_Context $block_editor_context
**Since:** 5.8 | **Tags:** #Recent
Filters the default array of categories for block types.

### block_editor_settings_all
**Params:** array $editor_settings, WP_Block_Editor_Context $block_editor_context
**Since:** 5.8 | **Tags:** #Recent
Filters the settings to pass to the block editor for all editor type.

### document_title
**Params:** string $title
**Since:** 5.8 | **Tags:** #Recent
Filters the document title.

### excerpt_allowed_wrapper_blocks
**Params:** string[] $allowed_wrapper_blocks
**Since:** 5.8 | **Tags:** #Recent
Filters the list of blocks that can be used as wrapper blocks, allowing excerpts to be generated from the `innerBlocks` of these wrappers.

### block_core_navigation_render_fallback
**Params:** array[] $fallback_blocks
**Since:** 5.9 | **Tags:** #Recent
Filters the fallback experience for the Navigation block. Returning a falsey value will opt out of the fallback and cause the block not to render. To customise the blocks provided return an array of blocks - these should be valid children of the `core/navigation` block.

### default_template_types
**Params:** array[] $default_template_types
**Since:** 5.9 | **Tags:** #Recent
Filters the list of default template types.

### default_wp_template_part_areas
**Params:** array[] $default_area_definitions
**Since:** 5.9 | **Tags:** #Recent
Filters the list of allowed template part area values.

### get_block_file_template
**Params:** WP_Block_Template|null $block_template, string $id, string $template_type
**Since:** 5.9 | **Tags:** #Recent
Filters the block template object after it has been (potentially) fetched from the theme file.

### get_block_template
**Params:** WP_Block_Template|null $block_template, string $id, string $template_type
**Since:** 5.9 | **Tags:** #Recent
Filters the queried block template object after it's been fetched.

### get_block_templates
**Params:** WP_Block_Template[] $query_result, array $query, string $template_type
**Since:** 5.9 | **Tags:** #Recent
Filters the array of queried block templates array after they've been fetched.

### pre_get_block_file_template
**Params:** WP_Block_Template|null $block_template, string $id, string $template_type
**Since:** 5.9 | **Tags:** #Recent
Filters the block template object before the theme file discovery takes place. Return a non-null value to bypass the WordPress theme file discovery.

### pre_get_block_template
**Params:** WP_Block_Template|null $block_template, string $id, string $template_type
**Since:** 5.9 | **Tags:** #Recent
Filters the block template object before the query takes place. Return a non-null value to bypass the WordPress queries.

### pre_get_block_templates
**Params:** WP_Block_Template[]|null $block_templates, array $query, string $template_type
**Since:** 5.9 | **Tags:** #Recent
Filters the block templates array before the query takes place. Return a non-null value to bypass the WordPress queries.

### rss_widget_feed_link
**Params:** string|false $feed_link, array $instance
**Since:** 5.9 | **Tags:** #Recent
Filters the classic RSS widget's feed icon link. Themes can remove the icon link by using `add_filter( 'rss_widget_feed_link', '__return_empty_string' );`.

### term_exists_default_query_args
**Params:** array $defaults, int|string $term, string $taxonomy, int|null $parent_term
**Since:** 6.0 | **Tags:** #Recent
Filters default query arguments for checking if a term exists.

### block_core_navigation_render_inner_blocks
**Params:** \WP_Block_List $inner_blocks
**Since:** 6.1 | **Tags:** #Recent
Filter navigation block $inner_blocks. Allows modification of a navigation block menu items.

### feed_links_extra_show_author_feed
**Params:** bool $show
**Since:** 6.1 | **Tags:** #Recent
Filters whether to display the author feed link.

### feed_links_extra_show_category_feed
**Params:** bool $show
**Since:** 6.1 | **Tags:** #Recent
Filters whether to display the category feed link.

### feed_links_extra_show_post_comments_feed
**Params:** bool $show_comments_feed
**Since:** 6.1 | **Tags:** #Recent
Filters whether to display the post comments feed link. This filter allows to enable or disable the feed link for a singular post in a way that is independent of {@see 'feed_links_show_comments_feed'} (which controls the global comments feed). The result of that filter is accepted as a parameter.

### feed_links_extra_show_post_type_archive_feed
**Params:** bool $show
**Since:** 6.1 | **Tags:** #Recent
Filters whether to display the post type archive feed link.

### feed_links_extra_show_search_feed
**Params:** bool $show
**Since:** 6.1 | **Tags:** #Recent
Filters whether to display the search results feed link.

### feed_links_extra_show_tag_feed
**Params:** bool $show
**Since:** 6.1 | **Tags:** #Recent
Filters whether to display the tag feed link.

### feed_links_extra_show_tax_feed
**Params:** bool $show
**Since:** 6.1 | **Tags:** #Recent
Filters whether to display the custom taxonomy feed link.

### post_class_taxonomies
**Params:** string[] $taxonomies, int $post_id, string[] $classes, string[] $css_class
**Since:** 6.1 | **Tags:** #Recent
Filters the taxonomies to generate classes for each individual term. Default is all public taxonomies registered to the post type.

### pre_wp_list_authors_post_counts_query
**Params:** int[]|false $post_counts, array $parsed_args
**Since:** 6.1 | **Tags:** #Recent
Filters whether to short-circuit performing the query for author post counts.

### the_posts_pagination_args
**Params:** array $args
**Since:** 6.1 | **Tags:** #Recent
Filters the arguments for posts pagination links.

### wp_list_authors_args
**Params:** array $query_args, array $parsed_args
**Since:** 6.1 | **Tags:** #Recent
Filters the query arguments for the list of all authors of the site.

### wp_list_table_class_name
**Params:** string $class_name, array $args
**Since:** 6.1 | **Tags:** #Recent
Filters the list table class to instantiate.

### wp_list_users_args
**Params:** array $query_args, array $parsed_args
**Since:** 6.1 | **Tags:** #Recent
Filters the query arguments for the list of all users of the site.

### post_search_columns
**Params:** string[] $search_columns, string $search, WP_Query $query
**Since:** 6.2 | **Tags:** #Recent
Filters the columns to search in a WP_Query search. The supported columns are `post_title`, `post_excerpt` and `post_content`. They are all included by default.

### get_pages_query_args
**Params:** array $query_args, array $parsed_args
**Since:** 6.3 | **Tags:** #Recent
Filters query arguments passed to WP_Query in get_pages().

### nav_menu_item_attributes
**Params:** array $li_atts, WP_Post $menu_item, stdClass $args, int $depth
**Since:** 6.3 | **Tags:** #Recent
Filters the HTML attributes applied to a menu's list item element.

### nav_menu_submenu_attributes
**Params:** array $atts, stdClass $args, int $depth
**Since:** 6.3 | **Tags:** #Recent
Filters the HTML attributes applied to a menu list element.

### pre_wp_setup_nav_menu_item
**Params:** object|null $modified_menu_item, object $menu_item
**Since:** 6.3 | **Tags:** #Recent
Filters whether to short-circuit the wp_setup_nav_menu_item() output. Returning a non-null value from the filter will short-circuit wp_setup_nav_menu_item(), returning that value instead.

### site_editor_no_javascript_message
**Params:** string $message, WP_Post $post
**Since:** 6.3 | **Tags:** #Recent
Filters the message displayed in the site editor interface when JavaScript is not enabled in the browser.

### block_widgets_no_javascript_message
**Params:** string $message, bool $installed
**Since:** 6.4 | **Tags:** #Recent
Filters the message displayed in the block widget interface when JavaScript is not enabled in the browser.

### hooked_block_types
**Params:** string[] $hooked_block_types, string $relative_position, string $anchor_block_type, WP_Block_Template|WP_Post|array $context
**Since:** 6.4 | **Tags:** #Recent
Filters the list of hooked block types for a given anchor block type and relative position.

### block_core_navigation_listable_blocks
**Params:** array $needs_list_item_wrapper
**Since:** 6.5 | **Tags:** #Recent
Filter the list of blocks that need a list item wrapper. Affords the ability to customize which blocks need a list item wrapper when rendered within a core/navigation block. This is useful for blocks that are not list items but should be wrapped in a list item when used as a child of a navigation block.

### get_block_type_uses_context
**Params:** string[] $uses_context, WP_Block_Type $block_type
**Since:** 6.5 | **Tags:** #Recent
Filters the registered uses context for a block type.

### get_block_type_variations
**Params:** array $variations, WP_Block_Type $block_type
**Since:** 6.5 | **Tags:** #Recent
Filters the registered variations for a block type.

### hooked_block
**Params:** array|null $parsed_hooked_block, string $hooked_block_type, string $relative_position, array $parsed_anchor_block, WP_Block_Template|WP_Post|array $context
**Since:** 6.5 | **Tags:** #Recent
Filters the parsed block array for a given hooked block.

### hooked_block_{$hooked_block_type}
**Since:** 6.5 | **Tags:** #Variable #Recent

### interactivity_process_directives
**Params:** bool $enabled
**Since:** 6.6 | **Tags:** #Recent
Filters whether Interactivity API should process directives.

### block_bindings_source_value
**Params:** mixed $value, string $name, array $source_args, WP_Block $block_instance, string $attribute_name
**Since:** 6.7 | **Tags:** #Recent
Filters the output of a block bindings source.

### feed_links_args
**Params:** array $args
**Since:** 6.7 | **Tags:** #Recent
Filters the feed links arguments.

### feed_links_extra_args
**Params:** array $args
**Since:** 6.7 | **Tags:** #Recent
Filters the extra feed links arguments.

### get_calendar_args
**Params:** array $args
**Since:** 6.8 | **Tags:** #Recent
Filter the `get_calendar` function arguments before they are used.

### render_block_core_navigation_link_allowed_post_status
**Params:** array $post_status, array $attributes, WP_Block $block
**Since:** 6.8 | **Tags:** #Recent
Filter allowed post_status for navigation link block to render.

### the_password_form_incorrect_password
**Params:** string $text, WP_Post $post
**Since:** 6.8 | **Tags:** #Recent
Filters the invalid password message shown on password-protected posts. The filter is only applied if the post is password-protected.

### block_bindings_supported_attributes
**Params:** string[] $supported_block_attributes, string $block_type
**Since:** 6.9 | **Tags:** #Recent
Filters the supported block attributes for block bindings.

### block_bindings_supported_attributes_{$block_type}
**Since:** 6.9 | **Tags:** #Variable #Recent

### block_core_social_link_get_services
**Params:** array $services_data
**Since:** 6.9 | **Tags:** #Recent
Filter the list of available social service. This can be used to change icons or add custom icons (additionally to variations in the editor). Icons should be directly renderable - therefore SVGs work best.

### enqueue_empty_block_content_assets
**Params:** bool $enqueue, string $block_name
**Since:** 6.9 | **Tags:** #Recent
Filters whether to enqueue assets for a block which has no rendered content.

### post_states_html
**Params:** string $post_states_html, WP_Post $post
**Since:** 6.9 | **Tags:** #Recent
Filters the HTML string of post states.

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
