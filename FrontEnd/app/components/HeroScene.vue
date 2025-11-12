<template>
  <div ref="container" class="hero-scene">
    <canvas ref="canvas" class="hero-scene__canvas" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, onBeforeUnmount, ref } from 'vue'
import * as THREE from 'three'

const props = withDefaults(
  defineProps<{
    colorA?: string
    colorB?: string
    density?: number
  }>(),
  {
    colorA: '#4463ff',
    colorB: '#38bdf8',
    density: 1
  }
)

const container = ref<HTMLDivElement | null>(null)
const canvas = ref<HTMLCanvasElement | null>(null)

let renderer: THREE.WebGLRenderer | null = null
let scene: THREE.Scene | null = null
let camera: THREE.PerspectiveCamera | null = null
let animationId: number | null = null
let points: THREE.Points | null = null

const resize = () => {
  if (!container.value || !renderer || !camera) return
  const { clientWidth, clientHeight } = container.value

  camera.aspect = clientWidth / clientHeight
  camera.updateProjectionMatrix()

  renderer.setSize(clientWidth, clientHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
}

onMounted(() => {
  if (!canvas.value || !container.value) {
    return
  }

  const { clientWidth, clientHeight } = container.value

  const density = Math.max(props.density, 0.15)
  const baseParticleCount = 1200
  const particleCount = Math.round(baseParticleCount * density)

  renderer = new THREE.WebGLRenderer({
    canvas: canvas.value,
    antialias: true,
    alpha: true
  })
  renderer.setSize(clientWidth, clientHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))

  scene = new THREE.Scene()

  camera = new THREE.PerspectiveCamera(45, clientWidth / clientHeight, 0.1, 50)
  camera.position.set(0, 0, 10)

  const geometry = new THREE.BufferGeometry()
  const positions = new Float32Array(particleCount * 3)
  const scales = new Float32Array(particleCount)

  for (let i = 0; i < particleCount; i += 1) {
    const i3 = i * 3
    const radius = THREE.MathUtils.randFloat(1.5, 4.5)
    const angle = THREE.MathUtils.randFloat(0, Math.PI * 2)
    const y = THREE.MathUtils.randFloatSpread(3.5)

    positions[i3] = Math.cos(angle) * radius
    positions[i3 + 1] = y
    positions[i3 + 2] = Math.sin(angle) * radius

    scales[i] = THREE.MathUtils.randFloat(0.4, 1.2)
  }

  geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))
  geometry.setAttribute('scale', new THREE.BufferAttribute(scales, 1))

  const material = new THREE.ShaderMaterial({
    uniforms: {
      uTime: { value: 0 },
      uColorA: { value: new THREE.Color(props.colorA) },
      uColorB: { value: new THREE.Color(props.colorB) }
    },
    vertexShader: `
      varying vec3 vPosition;
      varying float vScale;
      uniform float uTime;

      void main() {
        vec3 transformed = position;
        float wave = sin((transformed.y * 1.5) + (uTime * 1.2)) * 0.18;
        transformed.x += normal.x * wave;
        transformed.z += normal.z * wave;

        vec4 mvPosition = modelViewMatrix * vec4(transformed, 1.0);
        gl_PointSize = 30.0 * (1.0 / -mvPosition.z) * clamp(vScale, 0.6, 1.5);
        gl_Position = projectionMatrix * mvPosition;

        vPosition = transformed;
        vScale = clamp(vScale, 0.6, 1.5);
      }
    `,
    fragmentShader: `
      varying vec3 vPosition;
      varying float vScale;
      uniform vec3 uColorA;
      uniform vec3 uColorB;

      void main() {
        float d = length(gl_PointCoord - vec2(0.5));
        float alpha = smoothstep(0.6, 0.0, d);
        vec3 color = mix(uColorA, uColorB, vScale);
        gl_FragColor = vec4(color, alpha);
      }
    `,
    transparent: true,
    depthWrite: false,
    blending: THREE.AdditiveBlending
  })

  points = new THREE.Points(geometry, material)
  scene.add(points)

  const animate = () => {
    if (!renderer || !scene || !camera || !points) return

    const material = points.material as THREE.ShaderMaterial & {
      uniforms: { uTime: { value: number } }
    }
    material.uniforms.uTime.value += 0.01

    points.rotation.y += 0.0015
    points.rotation.x = Math.sin(material.uniforms.uTime.value * 0.2) * 0.08

    renderer.render(scene, camera)
    animationId = requestAnimationFrame(animate)
  }

  animate()
  window.addEventListener('resize', resize)
  resize()
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', resize)
  if (animationId) cancelAnimationFrame(animationId)

  if (scene) {
    scene.clear()
  }

  renderer?.dispose()
  renderer = null
  scene = null
  camera = null
  points = null
})
</script>

<style scoped>
.hero-scene {
  position: absolute;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  pointer-events: none;
}

.hero-scene__canvas {
  width: 100%;
  height: 100%;
  display: block;
  opacity: 0.95;
  filter: drop-shadow(0 0 60px rgba(59, 130, 246, 0.35));
}
</style>

