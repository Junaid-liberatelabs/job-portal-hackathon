# Lenis Smooth Scroll Integration

This project uses [Lenis](https://github.com/darkroomengineering/lenis) for smooth scrolling, based on the official documentation.

## Features

- ✅ Smooth scrolling with customizable easing
- ✅ Automatic anchor link handling
- ✅ Nested scroll prevention
- ✅ Route change handling
- ✅ Auto-resize on window resize
- ✅ Proper cleanup on unmount

## Usage

### Basic Usage

Lenis is automatically initialized on all pages. No additional setup required!

### Anchor Links

Anchor links work automatically with smooth scroll:

```html
<a href="#section-1">Go to Section 1</a>
<div id="section-1">...</div>
```

### Programmatic Scrolling

Access Lenis in your components:

```vue
<script setup>
const { $lenis } = useNuxtApp()

// Scroll to top
$lenis.scrollTo(0)

// Scroll to element
$lenis.scrollTo('#target')

// Scroll with options
$lenis.scrollTo('#target', {
  offset: -100,    // Offset from target (e.g., for fixed header)
  duration: 2,     // Animation duration in seconds
  immediate: false // Skip animation
})
</script>
```

### Nested Scroll (Prevent Lenis)

For scrollable containers inside the main scroll, prevent Lenis from capturing scroll events:

#### Prevent all scroll events:
```html
<div data-lenis-prevent>
  <!-- Scrollable content (modal, dropdown, etc.) -->
</div>
```

#### Prevent only wheel events:
```html
<div data-lenis-prevent-wheel>
  <!-- Content where wheel scroll should be native -->
</div>
```

#### Prevent only touch events:
```html
<div data-lenis-prevent-touch>
  <!-- Content where touch scroll should be native -->
</div>
```

### Control Lenis State

```vue
<script setup>
const { $lenis } = useNuxtApp()

// Stop smooth scrolling
$lenis.stop()

// Resume smooth scrolling
$lenis.start()

// Check if scrolling
console.log($lenis.isStopped) // boolean
</script>
```

### Listen to Scroll Events

```vue
<script setup>
const { $lenis } = useNuxtApp()

onMounted(() => {
  // Listen for scroll events
  $lenis.on('scroll', (e) => {
    console.log('Scroll position:', e.scroll)
    console.log('Scroll direction:', e.direction) // 1 or -1
    console.log('Velocity:', e.velocity)
  })
})
</script>
```

### Resize Manually (if autoResize is disabled)

```vue
<script setup>
const { $lenis } = useNuxtApp()

// Call resize when content changes
$lenis.resize()
</script>
```

## Configuration

Lenis is configured in `app/plugins/lenis.client.ts` with the following settings:

```typescript
{
  duration: 1.2,           // Animation duration
  easing: easeOutExpo,     // Easing function
  orientation: 'vertical', // Scroll direction
  smoothWheel: true,       // Smooth wheel scrolling
  wheelMultiplier: 1,      // Wheel scroll sensitivity
  infinite: false,         // Infinite scroll
  autoResize: true,        // Auto-resize on window resize
}
```

## Best Practices

### 1. Fixed Headers
When using fixed headers, use the `offset` option:

```vue
$lenis.scrollTo('#section', { offset: -80 })
```

### 2. GSAP ScrollTrigger Integration

If using GSAP ScrollTrigger, synchronize it with Lenis:

```vue
<script setup>
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const { $lenis } = useNuxtApp()

onMounted(() => {
  // Sync ScrollTrigger with Lenis
  $lenis.on('scroll', ScrollTrigger.update)

  gsap.ticker.add((time) => {
    $lenis.raf(time * 1000)
  })
})
</script>
```

### 3. Route Changes

Lenis automatically scrolls to top on route changes. To disable this behavior, modify `app/plugins/lenis.client.ts`.

### 4. Performance

- Lenis is lightweight (~2KB gzipped)
- Uses native `requestAnimationFrame` for 60fps smooth scrolling
- `smoothTouch` is disabled for better mobile performance
- Works on all modern browsers

## Troubleshooting

### Smooth scroll not working?

1. Check that the page is scrollable (content overflows viewport)
2. Verify Lenis is initialized (check browser console)
3. Make sure no other smooth scroll libraries are conflicting

### Nested scroll issues?

Use `data-lenis-prevent` on the nested scrollable container.

### Performance issues on mobile?

Touch scrolling is native by default (`smoothTouch: false`) for best performance.

## Resources

- [Official Lenis Repository](https://github.com/darkroomengineering/lenis)
- [Lenis Demo](https://lenis.darkroom.engineering)
- [Lenis Documentation](https://github.com/darkroomengineering/lenis#readme)

## License

Lenis is licensed under [MIT License](https://github.com/darkroomengineering/lenis/blob/main/LICENSE).

