<template>
  <div class="relative w-full overflow-hidden">
    <div ref="chartContainer" class="w-full" :style="{ height: height + 'px', minHeight: height + 'px' }"></div>
    <div v-if="loading" class="absolute inset-0 flex items-center justify-center bg-white/80 rounded-xl">
      <div class="animate-spin h-8 w-8 border-4 border-brand-500 border-t-transparent rounded-full"></div>
    </div>
    <div v-if="!loading && (!$echarts || !chartContainer)" class="absolute inset-0 flex items-center justify-center text-ink-400">
      <p class="text-sm">Chart loading...</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue'

interface SkillData {
  name: string
  value: number
  category?: string
}

interface Props {
  skills: SkillData[]
  title?: string
  chartType?: 'pie' | 'radar' | 'bar'
  height?: number
}

const props = withDefaults(defineProps<Props>(), {
  title: 'Skill Analysis',
  chartType: 'pie',
  height: 300
})

const { $echarts } = useNuxtApp()
const chartContainer = ref<HTMLElement | null>(null)
const loading = ref(false)
let chartInstance: any = null

const initChart = () => {
  if (!chartContainer.value || !$echarts) {
    console.warn('Chart container or ECharts not available')
    return
  }

  try {
    chartInstance = $echarts.init(chartContainer.value)

    const option = getChartOption()
    chartInstance.setOption(option)

    window.addEventListener('resize', handleResize)
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
        formatter: '{b}: {c} ({d}%)',
        confine: true
      },
      legend: {
        orient: 'vertical',
        left: '5%',
        top: 'center',
        textStyle: {
          fontSize: 11,
          color: '#4b5563'
        },
        itemGap: 8,
        itemWidth: 14,
        itemHeight: 14,
        formatter: (name: string) => {
          // Truncate long names
          return name.length > 15 ? name.substring(0, 15) + '...' : name
        }
      },
      series: [{
        name: 'Skills',
        type: 'pie',
        radius: ['45%', '70%'],
        center: ['60%', '50%'],
        avoidLabelOverlap: true,
        itemStyle: {
          borderRadius: 8,
          borderColor: '#fff',
          borderWidth: 2
        },
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 14,
            fontWeight: 'bold'
          },
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        },
        labelLine: {
          show: false
        },
        data: props.skills.map((skill, index) => ({
          value: skill.value,
          name: skill.name,
          itemStyle: {
            color: colors[index % colors.length]
          }
        }))
      }]
    }
  }

  if (props.chartType === 'radar') {
    return {
      color: colors,
      tooltip: {
        trigger: 'item',
        confine: true
      },
      radar: {
        indicator: props.skills.map(skill => ({
          name: skill.name.length > 12 ? skill.name.substring(0, 12) + '...' : skill.name,
          max: 100
        })),
        shape: 'polygon',
        splitNumber: 5,
        radius: '65%',
        center: ['50%', '50%'],
        axisName: {
          color: '#4b5563',
          fontSize: 10,
          fontWeight: 500
        },
        splitLine: {
          lineStyle: {
            color: '#e5e7eb'
          }
        },
        splitArea: {
          show: true,
          areaStyle: {
            color: ['rgba(59, 130, 246, 0.05)', 'rgba(59, 130, 246, 0.1)']
          }
        },
        axisLine: {
          lineStyle: {
            color: '#d1d5db'
          }
        }
      },
      series: [{
        name: 'Skill Level',
        type: 'radar',
        symbol: 'circle',
        symbolSize: 6,
        data: [{
          value: props.skills.map(skill => skill.value),
          name: 'Your Skills',
          areaStyle: {
            color: 'rgba(59, 130, 246, 0.25)'
          },
          lineStyle: {
            color: '#3b82f6',
            width: 2
          },
          itemStyle: {
            color: '#3b82f6',
            borderColor: '#fff',
            borderWidth: 2
          }
        }]
      }]
    }
  }

  // Bar chart
  return {
    color: colors,
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      },
      formatter: '{b}: {c}%',
      confine: true
    },
    grid: {
      left: '15px',
      right: '20px',
      bottom: '15px',
      top: '15px',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      max: 100,
      min: 0,
      axisLabel: {
        formatter: '{value}%',
        fontSize: 10,
        color: '#6b7280'
      },
      splitLine: {
        lineStyle: {
          color: '#e5e7eb',
          type: 'dashed'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#d1d5db'
        }
      }
    },
    yAxis: {
      type: 'category',
      data: props.skills.map(skill => 
        skill.name.length > 15 ? skill.name.substring(0, 15) + '...' : skill.name
      ),
      axisLabel: {
        fontSize: 11,
        color: '#4b5563',
        fontWeight: 500
      },
      axisLine: {
        lineStyle: {
          color: '#d1d5db'
        }
      }
    },
    series: [{
      name: 'Proficiency',
      type: 'bar',
      data: props.skills.map((skill, index) => ({
        value: skill.value,
        itemStyle: {
          color: colors[index % colors.length],
          borderRadius: [0, 4, 4, 0]
        }
      })),
      barWidth: '60%',
      barMaxWidth: 40,
      label: {
        show: false
      },
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }]
  }
}

const handleResize = () => {
  if (chartInstance) {
    chartInstance.resize()
  }
}

watch(() => props.skills, () => {
  if (chartInstance) {
    const option = getChartOption()
    chartInstance.setOption(option, true)
  }
}, { deep: true })

onMounted(() => {
  // Add a small delay to ensure DOM and ECharts are fully loaded
  setTimeout(() => {
    initChart()
  }, 100)
})

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.dispose()
    chartInstance = null
  }
  window.removeEventListener('resize', handleResize)
})
</script>

