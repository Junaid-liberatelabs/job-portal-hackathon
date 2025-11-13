<template>
  <Card :title="title" variant="default">
    <div ref="chartContainer" class="w-full" :style="{ height: height + 'px' }"></div>
    <div v-if="loading" class="absolute inset-0 flex items-center justify-center bg-white/80">
      <div class="animate-spin h-8 w-8 border-4 border-accent border-t-transparent rounded-full"></div>
    </div>
  </Card>
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
  if (!chartContainer.value || !$echarts) return

  chartInstance = $echarts.init(chartContainer.value)

  const option = getChartOption()
  chartInstance.setOption(option)

  window.addEventListener('resize', handleResize)
}

const getChartOption = () => {
  const colors = ['#4ecdc4', '#ff6b6b', '#3b82f6', '#f59e0b', '#10b981', '#8b5cf6']

  if (props.chartType === 'pie') {
    return {
      tooltip: {
        trigger: 'item',
        formatter: '{b}: {c} ({d}%)'
      },
      legend: {
        orient: 'vertical',
        left: 'left',
        textStyle: {
          fontSize: 12
        }
      },
      series: [{
        name: 'Skills',
        type: 'pie',
        radius: ['40%', '70%'],
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
            fontSize: 16,
            fontWeight: 'bold'
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
      tooltip: {
        trigger: 'item'
      },
      radar: {
        indicator: props.skills.map(skill => ({
          name: skill.name,
          max: 100
        })),
        shape: 'polygon',
        splitNumber: 5,
        axisName: {
          color: '#4b5563',
          fontSize: 11
        },
        splitLine: {
          lineStyle: {
            color: '#e5e7eb'
          }
        },
        splitArea: {
          show: true,
          areaStyle: {
            color: ['rgba(78, 205, 196, 0.05)', 'rgba(78, 205, 196, 0.1)']
          }
        }
      },
      series: [{
        name: 'Skill Level',
        type: 'radar',
        data: [{
          value: props.skills.map(skill => skill.value),
          name: 'Your Skills',
          areaStyle: {
            color: 'rgba(78, 205, 196, 0.3)'
          },
          lineStyle: {
            color: '#4ecdc4',
            width: 2
          },
          itemStyle: {
            color: '#4ecdc4'
          }
        }]
      }]
    }
  }

  // Bar chart
  return {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      max: 100,
      axisLabel: {
        formatter: '{value}%'
      }
    },
    yAxis: {
      type: 'category',
      data: props.skills.map(skill => skill.name),
      axisLabel: {
        fontSize: 11
      }
    },
    series: [{
      name: 'Proficiency',
      type: 'bar',
      data: props.skills.map((skill, index) => ({
        value: skill.value,
        itemStyle: {
          color: colors[index % colors.length]
        }
      })),
      barWidth: '60%',
      itemStyle: {
        borderRadius: [0, 4, 4, 0]
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
  initChart()
})

onUnmounted(() => {
  if (chartInstance) {
    chartInstance.dispose()
    chartInstance = null
  }
  window.removeEventListener('resize', handleResize)
})
</script>

