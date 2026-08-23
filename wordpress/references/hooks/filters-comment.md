# WordPress Filters: Comments / Pingbacks / Trackbacks

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### comment_author
**Params:** string $comment_author, string $comment_id
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the comment author's name for display.

### comment_email
**Params:** string $comment_author_email, WP_Comment $comment
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the comment author's email for display. Care should be taken to protect the email address and assure that email harvesters do not capture your commenter's email address.

### comment_excerpt
**Params:** string $comment_excerpt, string $comment_id
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the comment excerpt for display.

### comment_text
**Params:** string $comment_text, WP_Comment|null $comment, array $args
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the text of a comment to be displayed.

### comment_url
**Params:** string $comment_author_url, string $comment_id
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the comment author's URL for display.

### comments_number
**Params:** string $comments_number_text, int $comments_number
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comments count for display.

### comments_rewrite_rules
**Params:** string[] $comments_rewrite
**Since:** 1.5.2 | **Tags:** #Legacy
Filters rewrite rules used for comment feed archives. Likely comments feed archives include `/comments/feed/` and `/comments/feed/atom/`.

### comments_template
**Params:** string $theme_template
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the path to the theme template file used for the comments template.

### comment_author_rss
**Params:** string $comment_author
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the current comment author for use in a feed.

### comment_edit_pre
**Params:** string $comment_content
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment content before editing.

### comment_moderation_subject
**Params:** string $subject, int $comment_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment moderation email subject.

### comment_moderation_text
**Params:** string $notify_message, int $comment_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment moderation email text.

### comment_notification_headers
**Params:** string $message_headers, string $comment_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment notification email headers.

### comment_notification_subject
**Params:** string $subject, string $comment_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment notification email subject.

### comment_notification_text
**Params:** string $notify_message, string $comment_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment notification email text.

### comment_save_pre
**Since:** 1.5.2 | **Tags:** #Legacy

### comment_text_rss
**Params:** string $comment_text
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the current comment content for use in a feed.

### get_comment_author
**Params:** string $comment_author, string $comment_id, WP_Comment $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the returned comment author name.

### get_comment_author_email
**Params:** string $comment_author_email, string $comment_id, WP_Comment $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment author's returned email address.

### get_comment_author_IP
**Params:** string $comment_author_ip, string $comment_id, WP_Comment $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment author's returned IP address.

### get_comment_author_link
**Params:** string $comment_author_link, string $comment_author, string $comment_id
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment author's link for display.

### get_comment_author_url
**Params:** string $comment_author_url, string|int $comment_id, WP_Comment|null $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment author's URL.

### get_comment_author_url_link
**Params:** string $comment_author_url_link
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment author's returned URL link.

### get_comment_date
**Params:** string|int $comment_date, string $format, WP_Comment $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the returned comment date.

### get_comment_excerpt
**Params:** string $comment_excerpt, string $comment_id, WP_Comment $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the retrieved comment excerpt.

### get_comment_ID
**Params:** string $comment_id, WP_Comment $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the returned comment ID.

### get_comment_text
**Params:** string $comment_text, WP_Comment $comment, array $args
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the text of a comment.

### get_comment_time
**Params:** string|int $comment_time, string $format, bool $gmt, bool $translate, WP_Comment $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the returned comment time.

### get_comment_type
**Params:** string $comment_type, string $comment_id, WP_Comment $comment
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the returned comment type.

### preprocess_comment
**Params:** array $commentdata
**Since:** 1.5.2 | **Tags:** #Legacy
Filters a comment's data before it is sanitized and inserted into the database.

### pre_comment_approved
**Params:** int|string|WP_Error $approved, array $commentdata
**Since:** 1.5.2 | **Tags:** #Legacy
Filters a comment's approval status before it is set.

### pre_comment_author_email
**Params:** string $author_email_cookie
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment author's email cookie before it is set. When this filter hook is evaluated in wp_filter_comment(), the comment author's email string is passed.

### pre_comment_author_name
**Params:** string $author_cookie
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment author's name cookie before it is set. When this filter hook is evaluated in wp_filter_comment(), the comment author's name string is passed.

### pre_comment_author_url
**Params:** string $author_url_cookie
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the comment author's URL cookie before it is set. When this filter hook is evaluated in wp_filter_comment(), the comment author's URL string is passed.

### pre_comment_content
**Since:** 1.5.2 | **Tags:** #Legacy

### pre_comment_user_agent
**Since:** 1.5.2 | **Tags:** #Legacy

### pre_comment_user_ip
**Since:** 1.5.2 | **Tags:** #Legacy

### comment_edit_redirect
**Params:** string $location, int $comment_id
**Since:** 2.0.11 | **Tags:** #Legacy
Filters the URI the user is redirected to after editing a comment in the admin.

### comment_post_redirect
**Since:** 2.0.11 | **Tags:** #Legacy

### comments_array
**Params:** array $comments, int $post_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the comments array.

### comment_flood_filter
**Params:** bool $bool, int $time_lastcomment, int $time_newcomment
**Since:** 2.1 | **Tags:** #Legacy
Filters the comment flood status.

### comment_feed_groupby
**Since:** 2.2 | **Tags:** #Legacy

### comment_feed_join
**Since:** 2.2 | **Tags:** #Legacy

### comment_feed_where
**Since:** 2.2 | **Tags:** #Legacy

### trackback_url
**Params:** string $trackback_url
**Since:** 2.2 | **Tags:** #Legacy
Filters the returned trackback URL.

### comments_open
**Params:** bool $comments_open, int $post_id
**Since:** 2.5 | **Tags:** #Legacy
Filters whether the current post is open for comments.

### comments_popup_link_attributes
**Params:** string $link_attributes
**Since:** 2.5 | **Tags:** #Legacy
Filters the comments link attributes for display.

### comment_status_links
**Params:** string[] $status_links
**Since:** 2.5 | **Tags:** #Legacy
Filters the comment status links.

### get_avatar
**Params:** string $avatar, mixed $id_or_email, int $size, string $default_value, string $alt, array $args
**Since:** 2.5 | **Tags:** #Legacy
Filters the HTML for a user's avatar.

### pings_open
**Params:** bool $pings_open, int $post_id
**Since:** 2.5 | **Tags:** #Legacy
Filters whether the current post is open for pings.

### avatar_defaults
**Params:** string[] $avatar_defaults
**Since:** 2.6 | **Tags:** #Legacy
Filters the default avatars. Avatars are stored in key/value pairs, where the key is option value, and the name is the displayed avatar name.

### comments_per_page
**Params:** int $comments_per_page, string $comment_status
**Since:** 2.6 | **Tags:** #Legacy
Filters the number of comments listed per page in the comments list table.

### comment_row_actions
**Params:** string[] $actions, WP_Comment $comment
**Since:** 2.6 | **Tags:** #Legacy
Filters the action links displayed for each comment in the Comments list table.

### default_avatar_select
**Params:** string $avatar_list
**Since:** 2.6 | **Tags:** #Legacy
Filters the HTML output of the default avatar list.

### cancel_comment_reply_link
**Params:** string $cancel_comment_reply_link, string $link_url, string $link_text
**Since:** 2.7 | **Tags:** #Legacy
Filters the cancel comment reply link HTML.

### comment_class
**Params:** string[] $classes, string[] $css_class, string $comment_id, WP_Comment $comment, int|WP_Post $post
**Since:** 2.7 | **Tags:** #Legacy
Filters the returned CSS classes for the current comment.

### comment_reply_link
**Params:** string $comment_reply_link, array $args, WP_Comment $comment, WP_Post $post
**Since:** 2.7 | **Tags:** #Legacy
Filters the comment reply link.

### thread_comments_depth_max
**Params:** int $max_depth
**Since:** 2.7 | **Tags:** #Legacy
Filters the maximum depth of threaded/nested comments.

### wp_comment_reply
**Params:** string $content, array $args
**Since:** 2.7 | **Tags:** #Legacy
Filters the in-line comment reply-to form output in the Comments list table. Returning a non-empty value here will short-circuit display of the in-line comment-reply form in the Comments list table, echoing the returned value instead.

### wp_count_comments
**Params:** array|stdClass $count, int $post_id
**Since:** 2.7 | **Tags:** #Legacy
Filters the comments count for a given post or the whole site.

### comment_cookie_lifetime
**Params:** int $seconds
**Since:** 2.8 | **Tags:** #Legacy
Filters the lifetime of the comment cookie in seconds.

### comment_feed_limits
**Since:** 2.8 | **Tags:** #Legacy

### comment_feed_orderby
**Since:** 2.8 | **Tags:** #Legacy

### comment_moderation_headers
**Params:** string $message_headers, int $comment_id
**Since:** 2.8 | **Tags:** #Legacy
Filters the comment moderation email headers.

### get_comment_link
**Params:** string $comment_link, WP_Comment $comment, array $args, int $cpage
**Since:** 2.8 | **Tags:** #Legacy
Filters the returned single comment permalink.

### pingback_useragent
**Params:** string $concat_useragent, string $useragent, string $pingback_server_url, string $pagelinkedto, string $pagelinkedfrom
**Since:** 2.9 | **Tags:** #Legacy
Filters the user agent sent when pinging-back a URL.

### comment_form_defaults
**Params:** array $defaults
**Since:** 3.0 | **Tags:** #Modern
Filters the comment form default arguments. Use {@see 'comment_form_default_fields'} to filter the comment fields.

### comment_form_default_fields
**Params:** string[] $fields
**Since:** 3.0 | **Tags:** #Modern
Filters the default comment form fields.

### comment_form_field_comment
**Params:** string $args_comment_field
**Since:** 3.0 | **Tags:** #Modern
Filters the content of the comment textarea field for display.

### comment_form_field_{$name}
**Since:** 3.0 | **Tags:** #Variable #Modern

### comment_form_logged_in
**Params:** string $args_logged_in, array $commenter, string $user_identity
**Since:** 3.0 | **Tags:** #Modern
Filters the 'logged in' message for the comment form for display.

### comment_id_fields
**Params:** string $comment_id_fields, int $post_id, int $reply_to_id
**Since:** 3.0 | **Tags:** #Modern
Filters the returned comment ID fields.

### comment_max_links_url
**Params:** int $num_links, string $url, string $comment
**Since:** 3.0 | **Tags:** #Modern
Filters the number of links found in a comment.

### get_avatar_comment_types
**Params:** array $types
**Since:** 3.0 | **Tags:** #Modern
Filters the list of allowed comment types for retrieving avatars.

### comments_clauses
**Since:** 3.1 | **Tags:** #Modern

### the_comments
**Since:** 3.1 | **Tags:** #Modern

### wp_get_current_commenter
**Params:** array $comment_author_data
**Since:** 3.1 | **Tags:** #Modern
Filters the current commenter's name, email, and URL.

### close_comments_for_post_types
**Params:** string[] $post_types
**Since:** 3.2 | **Tags:** #Modern
Filters the list of post types to automatically close comments for.

### comments_link_feed
**Params:** string $comment_permalink
**Since:** 3.6 | **Tags:** #Modern
Filters the comments permalink for the current post.

### comment_link
**Params:** string $comment_permalink
**Since:** 3.6 | **Tags:** #Modern
Filters the current comment's permalink.

### pingback_ping_source_uri
**Params:** string $pagelinkedfrom, string $pagelinkedto
**Since:** 3.6 | **Tags:** #Modern
Filters the pingback source URI.

### comment_moderation_recipients
**Params:** string[] $emails, int $comment_id
**Since:** 3.7 | **Tags:** #Modern
Filters the list of recipients for comment moderation emails.

### comment_notification_recipients
**Params:** string[] $emails, string $comment_id
**Since:** 3.7 | **Tags:** #Modern
Filters the list of email addresses to receive a comment notification. By default, only post authors are notified of comments. This filter allows others to be added.

### comment_notification_notify_author
**Params:** bool $notify, string $comment_id
**Since:** 3.8 | **Tags:** #Modern
Filters whether to notify comment authors of their comments on their own posts. By default, comment authors aren't notified of their comments on their own posts. This filter allows you to override that.

### comment_reply_link_args
**Params:** array $args, WP_Comment $comment, WP_Post $post
**Since:** 4.1 | **Tags:** #Modern
Filters the comment reply link arguments.

### comment_form_submit_button
**Params:** string $submit_button, array $args
**Since:** 4.2 | **Tags:** #Modern
Filters the submit button for the comment form to display.

### comment_form_submit_field
**Params:** string $submit_field, array $args
**Since:** 4.2 | **Tags:** #Modern
Filters the submit field for the comment form to display. The submit field includes the submit button, hidden fields for the comment form, and any wrapper markup.

### comment_excerpt_length
**Params:** int $comment_excerpt_length
**Since:** 4.4 | **Tags:** #Modern
Filters the maximum number of words used in the comment excerpt.

### comment_form_fields
**Params:** array $comment_fields
**Since:** 4.4 | **Tags:** #Modern
Filters the comment form fields, including the textarea.

### found_comments_query
**Params:** string $found_comments_query, WP_Comment_Query $comment_query
**Since:** 4.4 | **Tags:** #Modern
Filters the query used to retrieve found comment count.

### comments_template_query_args
**Params:** array $comment_args
**Since:** 4.5 | **Tags:** #Modern
Filters the arguments used to query comments in comments_template().

### comments_list_table_query_args
**Params:** array $args
**Since:** 5.1 | **Tags:** #Recent
Filters the arguments for the comment query in the comments list table.

### comment_duplicate_message
**Params:** string $comment_duplicate_message
**Since:** 5.2 | **Tags:** #Recent
Filters duplicate comment error message.

### comment_flood_message
**Params:** string $comment_flood_message
**Since:** 5.2 | **Tags:** #Recent
Filters the comment flood error message.

### comments_pre_query
**Since:** 5.3 | **Tags:** #Recent

### comments_template_top_level_query_args
**Params:** array $top_level_args
**Since:** 5.6 | **Tags:** #Recent
Filters the arguments used in the top level comments query.

### comment_author_link_rel
**Params:** string[] $rel_parts, WP_Comment $comment
**Since:** 6.2 | **Tags:** #Recent
Filters the rel attributes of the comment author's link.

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
