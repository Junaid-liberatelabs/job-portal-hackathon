<template>
  <div class="relative w-full h-full flex items-center justify-center">
    <div 
      ref="chartContainer" 
      class="w-full h-full" 
      :style="{ height: height + 'px', minHeight: height + 'px', width: '100%' }"
    ></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, nextTick } from 'vue'

interface SkillData {
  name: string
  value: number
  category?: string
}

interface Props {
  skills: SkillData[]
  title?: string
  chartType?: 'pie'
  height?: number
}

const props = withDefaults(defineProps<Props>(), {
  title: 'Skill Visualization',
  chartType: 'pie',
  height: 400
})

const { $echarts } = useNuxtApp()
const chartContainer = ref<HTMLElement | null>(null)
let chartInstance: any = null

const initChart = () => {
  if (!chartContainer.value) {
    console.warn('Chart container not available')
    return
  }

  if (!$echarts) {
    console.error('ECharts not loaded! Make sure echarts.client.ts plugin is working')
    return
  }

  // Check if skills data is available
  if (!props.skills || props.skills.length === 0) {
    console.warn('No skills data available for chart')
    return
  }

  try {
    console.log('Initializing chart with', props.skills.length, 'skills, type:', props.chartType)
    
    // Dispose existing instance if any
    if (chartInstance) {
      chartInstance.dispose()
    }
    
    chartInstance = $echarts.init(chartContainer.value)
    
    const option = getChartOption()
    console.log('Chart option generated for', props.chartType)
    chartInstance.setOption(option, true)

    window.addEventListener('resize', handleResize)
    console.log('Chart initialized successfully')
  } catch (error) {
    console.error('Error initializing chart:', error)
  }
}

const getChartOption = () => {
  // Brand-consistent blue gradient palette
  const colors = ['#3b82f6', '#60a5fa', '#2563eb', '#1d4ed8', '#93c5fd', '#1e40af', '#3b82f6']

  if (props.chartType === 'pie') {
    return {
      color: colors,
      tooltip: {
        trigger: 'item',
        formatter: '{b}',
        confine: true
      },
      series: [{
        name: 'Skills',
        type: 'pie',
        radius: ['35%', '60%'],
        center: ['50%', '50%'],
        avoidLabelOverlap: true,
        itemStyle: {
          borderRadius: 10,
          borderColor: '#fff',
          borderWidth: 3
        },
        label: {
          show: true,
          position: 'outside',
          formatter: '{b}',
          fontSize: 13,
          color: '#4b5563',
          fontWeight: 500,
          distanceToLabelLine: 5,
          alignTo: 'none'
        },
        labelLine: {
          show: true,
          length: 25,
          length2: 20,
          smooth: 0.3,
          lineStyle: {
            width: 2,
            color: '#d1d5db'
          }
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 16,
            fontWeight: 'bold',
            color: '#1e293b'
          },
          itemStyle: {
            shadowBlur: 15,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.3)'
          },
          scale: true,
          scaleSize: 10
        },
        data: props.skills.map((skill, index) => ({
          value: 1,  // Equal slices for all skills
          name: skill.name,
          itemStyle: {
            color: colors[index % colors.length]
          }
        }))
      }]
    }
  }
  
  // Default to pie chart
  return {
    color: colors,
    tooltip: {
      trigger: 'item',
      formatter: '{b}',
      confine: true
    },
    series: [{
      name: 'Skills',
      type: 'pie',
      radius: ['35%', '60%'],
      center: ['50%', '50%'],
      avoidLabelOverlap: true,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#fff',
        borderWidth: 3
      },
      label: {
        show: true,
        position: 'outside',
        formatter: '{b}',
        fontSize: 13,
        color: '#4b5563',
        fontWeight: 500,
        distanceToLabelLine: 5,
        alignTo: 'none'
      },
      labelLine: {
        show: true,
        length: 25,
        length2: 20,
        smooth: 0.3,
        lineStyle: {
          width: 2,
          color: '#d1d5db'
        }
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 16,
          fontWeight: 'bold',
          color: '#1e293b'
        },
        itemStyle: {
          shadowBlur: 15,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.3)'
        },
        scale: true,
        scaleSize: 10
      },
      data: props.skills.map((skill, index) => ({
        value: 1,
        name: skill.name,
        itemStyle: {
          color: colors[index % colors.length]
        }
      }))
    }]
  }
}

const handleResize = () => {
  if (chartInstance) {
    chartInstance.resize()
  }
}

// Watch for skills changes
watch(() => props.skills, () => {
  if (chartInstance) {
    const option = getChartOption()
    chartInstance.setOption(option, true)
  } else {
    // If chart instance doesn't exist, try to initialize
    setTimeout(() => initChart(), 150)
  }
}, { deep: true })

// Chart type watcher removed - only pie chart supported now

onMounted(async () => {
  // Initialize chart immediately when component mounts
  if (typeof window !== 'undefined') {
    // Wait for DOM to be fully ready
    await nextTick()
    
    // Use requestAnimationFrame to ensure layout is calculated
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        initChart()
        
        // Force resize after initialization to ensure proper dimensions
        setTimeout(() => {
          if (chartInstance) {
            chartInstance.resize()
          }
        }, 100)
        
        // Fallback attempt if first initialization failed
        setTimeout(() => {
          if (!chartInstance && chartContainer.value) {
            initChart()
            setTimeout(() => {
              if (chartInstance) {
                chartInstance.resize()
              }
            }, 100)
          }
        }, 500)
      })
    })
  }
})

// Add visibility change watcher to handle tab switching
if (typeof window !== 'undefined') {
  watch(() => chartContainer.value, (newVal) => {
    if (newVal && !chartInstance) {
      setTimeout(() => {
        initChart()
        setTimeout(() => {
          if (chartInstance) {
            chartInstance.resize()
          }
        }, 100)
      }, 250)
    }
  })
}

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.dispose()
    chartInstance = null
  }
  window.removeEventListener('resize', handleResize)
})
</script>

