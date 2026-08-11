# Forms & Validation

`v-model` on native inputs, modifier semantics, IME handling, custom form controls, and validation strategy.

## 1. `v-model` on Native Inputs

`v-model` expands to the right prop/event pair per input type:

| Element | Binds | Listens |
|---|---|---|
| `<input type="text">`, `<textarea>` | `value` | `input` |
| `<input type="checkbox">` | `checked` | `change` |
| `<input type="radio">` | `checked` | `change` |
| `<select>` | `value` | `change` |

```vue
<input v-model="form.email" type="email">
<textarea v-model="form.bio"></textarea>
<input v-model="form.agreed" type="checkbox">
<input v-model="form.plan" type="radio" value="pro">
<select v-model="form.country"><option value="tr">Türkiye</option></select>
<select v-model="form.tags" multiple><!-- array --></select>
```

### `v-model` ignores HTML value attributes

```vue
<!-- ❌ "Ada" never appears; v-model overwrites it with the bound value -->
<input v-model="name" value="Ada">

<!-- ✅ set the initial value in state -->
<script setup lang="ts">
const name = ref('Ada')
</script>
<input v-model="name">
```

Same for `checked` on checkboxes/radios and `selected` on options.

### `<textarea>` does not interpolate

```vue
<!-- ❌ ignored -->
<textarea>{{ text }}</textarea>

<!-- ✅ -->
<textarea v-model="text"></textarea>
```

## 2. Modifiers

```vue
<input v-model.trim="username">
<input v-model.number="quantity" type="number">
<input v-model.lazy="search">   <!-- syncs on change, not input -->
```

### `.number` pitfalls

- An empty input yields `''`, **not** `0` — `qty * price` becomes `NaN`.
- If the string cannot be parsed, the original string is kept.
- `type="number"` already coerces in most browsers; `.number` is still needed for `type="text"`.

```ts
const quantity = ref<number | ''>(1)
const safeQuantity = computed(() => (quantity.value === '' ? 0 : Number(quantity.value)))
```

### `.lazy` and search inputs

`.lazy` waits for `change` (blur/enter). For live search, keep the default `input` binding and debounce:

```ts
import { refDebounced } from '@vueuse/core'
const query = ref('')
const debouncedQuery = refDebounced(query, 300)
watch(debouncedQuery, runSearch)
```

## 3. IME Composition (CJK Input)

`v-model` deliberately does **not** update during IME composition. Live search/validation bound only to `v-model` appears broken for Chinese, Japanese, and Korean users.

```vue
<script setup lang="ts">
const query = ref('')
let composing = false

function onInput(e: Event) {
  const value = (e.target as HTMLInputElement).value
  if (!composing) query.value = value
  else liveQuery.value = value      // separate ref for preview, if desired
}
</script>

<template>
  <input
    :value="query"
    @input="onInput"
    @compositionstart="composing = true"
    @compositionend="e => { composing = false; onInput(e) }"
  >
</template>
```

Decide deliberately: search-as-you-type usually wants intermediate values; validation usually does not.

## 4. Checkboxes

```vue
<!-- Boolean -->
<input v-model="agreed" type="checkbox">

<!-- Custom values -->
<input v-model="notify" type="checkbox" true-value="yes" false-value="no">

<!-- Array of selected values -->
<input v-model="selectedIds" type="checkbox" value="a">
<input v-model="selectedIds" type="checkbox" value="b">
```

`true-value`/`false-value` are **Vue bindings, not HTML attributes** — they are not submitted by a native form POST. If the form is submitted natively, add a hidden input or submit via JavaScript.

## 5. `<select>` Initial Value

If the bound value does not match any option, the select renders in an unselected state. On iOS this makes the first option unselectable, because tapping it fires no `change` event.

```vue
<!-- ✅ provide a disabled placeholder as the initial value -->
<select v-model="country">
  <option disabled value="">Select a country</option>
  <option value="tr">Türkiye</option>
</select>
```

Initialize `country` to `''` so the placeholder is genuinely selected.

## 6. Custom Form Controls

```vue
<!-- BaseInput.vue -->
<script setup lang="ts">
defineOptions({ inheritAttrs: false })

const model = defineModel<string>()
const props = defineProps<{ label: string; error?: string; hint?: string }>()

const id = useId()
const errorId = `${id}-error`
const hintId = `${id}-hint`
</script>

<template>
  <div class="field" :class="{ 'field--invalid': !!error }">
    <label :for="id">{{ label }}</label>
    <input
      :id="id"
      v-model="model"
      v-bind="$attrs"
      :aria-invalid="!!error || undefined"
      :aria-describedby="[error && errorId, hint && hintId].filter(Boolean).join(' ') || undefined"
    >
    <p v-if="hint" :id="hintId" class="hint">{{ hint }}</p>
    <p v-if="error" :id="errorId" class="error" role="alert">{{ error }}</p>
  </div>
</template>
```

Key points:

- `defineModel` gives a real `v-model` contract including modifier support.
- `inheritAttrs: false` + `v-bind="$attrs"` puts `placeholder`, `type`, `required`, `autocomplete` on the `<input>`, not the wrapper `<div>`.
- `useId()` (Vue 3.5+) produces SSR-stable ids for label/`aria-describedby` wiring.

## 7. Validation

### Manual, for simple forms

```ts
const form = reactive({ email: '', password: '' })
const touched = reactive({ email: false, password: false })

const errors = computed(() => ({
  email: !form.email ? 'Required' : !form.email.includes('@') ? 'Invalid email' : '',
  password: form.password.length < 8 ? 'At least 8 characters' : '',
}))

const isValid = computed(() => Object.values(errors.value).every(e => !e))

function visibleError(field: keyof typeof form) {
  return touched[field] || submitted.value ? errors.value[field] : ''
}
```

Show errors on blur or after the first submit — never while the user is still typing their first character.

### Schema-based, for real forms

```ts
import { z } from 'zod'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'

const schema = toTypedSchema(z.object({
  email: z.string().email(),
  password: z.string().min(8),
  age: z.coerce.number().int().min(18),
}))

const { handleSubmit, errors, defineField, isSubmitting } = useForm({
  validationSchema: schema,
})

const [email, emailAttrs] = defineField('email')

const onSubmit = handleSubmit(async (values) => {
  await api.auth.register(values)   // values are fully typed from the schema
})
```

The same Zod schema can validate the API response, keeping one source of truth for the shape.

### Server errors

```ts
try {
  await api.auth.register(values)
} catch (e) {
  if (e instanceof ApiError && e.status === 422) {
    setErrors(e.body.errors)      // map field-level server errors back to the form
  } else {
    formError.value = 'Something went wrong. Please try again.'
  }
}
```

Always render a form-level error for non-field failures — a silently failing submit button is a common bug.

## 8. Submission

```vue
<form novalidate @submit.prevent="onSubmit">
  <BaseInput v-model="email" label="Email" :error="errors.email" type="email" autocomplete="email">
  <button type="submit" :disabled="isSubmitting">
    {{ isSubmitting ? 'Saving…' : 'Save' }}
  </button>
</form>
```

- `@submit.prevent` — never bind submit to a `@click` on the button; that breaks Enter-to-submit.
- Disable the submit button while in flight to prevent double submission (and guard server-side too).
- `novalidate` when you own the validation UI, so browser bubbles do not compete with your messages.
- Reset `touched`/`submitted` state after a successful submit.

## 9. Accessibility Checklist

- [ ] Every control has a `<label for>` (or is wrapped by its label) — placeholders are not labels
- [ ] `autocomplete` set on name/email/address/password fields
- [ ] `aria-invalid` and `aria-describedby` wire errors to their fields
- [ ] Error messages use `role="alert"` (or live in an `aria-live` region)
- [ ] Focus moves to the first invalid field on failed submit
- [ ] Required fields marked in text, not only by color or an asterisk
- [ ] Submit state announced (`aria-busy` or a live region), not only a spinner
- [ ] `type="email"`/`tel"`/`url"` for correct mobile keyboards

## Anti-Patterns

| Anti-pattern | Consequence | Fix |
|---|---|---|
| `value="x"` with `v-model` | Initial value ignored | Set it in state |
| `{{ }}` in `<textarea>` | Content ignored | `v-model` |
| `.number` result used unguarded | `NaN` from empty input | Coerce with a computed |
| Live search bound only to `v-model` | Broken for CJK users | Handle composition events |
| `true-value` in a native form POST | Value never submitted | Hidden input or JS submit |
| Select bound to an unmatched value | iOS first option unselectable | Disabled placeholder + `''` |
| Wrapper without `inheritAttrs: false` | `placeholder`/`type` on the `<div>` | `inheritAttrs: false` + `$attrs` |
| Errors shown while typing | Hostile UX | Show on blur / after submit |
| `@click` on the submit button | Enter key does not submit | `@submit.prevent` on the form |
| No form-level error state | Silent failures | Render a non-field error |

## Sources

- [Vue — Form input bindings](https://vuejs.org/guide/essentials/forms.html)
- [VeeValidate](https://vee-validate.logaretm.com/v4/)
