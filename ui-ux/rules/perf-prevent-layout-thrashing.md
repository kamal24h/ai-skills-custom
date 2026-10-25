---
title: Batch DOM Reads and Writes to Prevent Layout Thrashing
impact: CRITICAL
impactDescription: Interleaving geometric style reads with DOM mutations forces the browser engine to perform costly synchronous layout calculations, dropping frame rates and causing UI freezes.
tags: performance, rendering, cwv, inp, javascript, dom
---

# Batch DOM Reads and Writes to Prevent Layout Thrashing

Layout thrashing (forced synchronous reflow) occurs when code queries computed geometry properties (like `offsetHeight`, `getBoundingClientRect()`, or `scrollTop`) immediately after modifying the DOM or inline styles. The browser is forced to flush pending layout changes synchronously to calculate the answer.

To maintain a fluid 60fps frame rate and achieve responsive INP (Interaction to Next Paint < 200ms), batch all DOM read operations together first, and then perform all DOM write operations.

## Bad Example

Interleaving reads and writes inside loops or event callbacks:

```javascript
// ❌ Forces synchronous layout recalculation on every single item
function updateHeights(elements) {
  elements.forEach(el => {
    const currentHeight = el.offsetHeight; // READ: forces layout
    el.style.height = `${currentHeight + 20}px`; // WRITE: invalidates layout
  });
}
```

## Good Example

Batching all reads before performing writes:

```javascript
// ✅ Performs exactly ONE layout calculation for the entire batch
function updateHeights(elements) {
  // 1. Batch all geometric reads
  const heights = elements.map(el => el.offsetHeight);

  // 2. Batch all style writes
  elements.forEach((el, index) => {
    el.style.height = `${heights[index] + 20}px`;
  });
}
```
