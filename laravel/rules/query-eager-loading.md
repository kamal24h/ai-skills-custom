---
title: Constrain Eager Loads — Select Columns, Limit Rows
impact: HIGH
impactDescription: "Cuts memory and transfer: only needed columns and rows are hydrated"
tags: eager-loading, with-constraints, column-selection, performance
---

## Constrain Eager Loads — Select Columns, Limit Rows

**Impact: HIGH (Only needed columns and rows get hydrated)**

The base N+1 fix is [`eloquent-eager-loading`](eloquent-eager-loading.md); automatic loading is covered by [`query-auto-eager-loading`](query-auto-eager-loading.md). This rule covers what to do *after* you eager load: an unconstrained `with('comments')` on a hot post still hydrates thousands of Eloquent models it never displays. Constrain every eager load on list endpoints — select the columns each view renders, cap related-row counts with `limit()`.

## Incorrect

```php
// ❌ Hydrates every column of every related row
$posts = Post::with(['author', 'comments'])->get();
// author rows: all columns including bio (TEXT), settings (JSON)
// comments per post: unbounded — a popular post loads 5,000 models
```

## Correct

```php
// ✅ Column selection + per-relationship constraints — 3 lean queries
$posts = Post::with([
    'author:id,name,avatar',                      // only rendered columns
    'comments' => fn ($q) => $q->latest()->limit(5), // capped preview rows
])->get();

// ✅ Counts instead of rows when the number is all you render
$posts = Post::withCount('comments')->get();      // $post->comments_count

foreach ($posts as $post) {
    echo $post->author->name;                     // hydrated, no extras
    echo $post->comments->pluck('body');          // at most 5 models each
}
```

**Benefits:**
- Memory drops with column count: TEXT/JSON columns never hydrate when unselected
- Row caps keep popular-parent queries O(1) regardless of related-row totals
- `withCount()` answers "how many?" without hydrating a single model

Reference: [Laravel Eager Loading — Constraining](https://laravel.com/docs/13.x/eloquent-relationships#constraining-eager-loads)
