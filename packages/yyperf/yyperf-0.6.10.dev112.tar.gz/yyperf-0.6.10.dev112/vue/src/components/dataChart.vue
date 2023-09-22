<template>
  <div v-if="count>0">
    <highcharts :options="chartOption" :constructor-type="'stockChart'" ref="chart"
                :updateArgs="[false, false]"
    ></highcharts>
  </div>
  <div v-else>
    <el-empty :description="'暂无'+title+'数据'"></el-empty>
  </div>

</template>
<script>
import {Chart} from 'highcharts-vue'
import Highcharts from 'highcharts'
import stockInit from 'highcharts/modules/stock'
import boostInt from 'highcharts/modules/boost'

Highcharts.setOptions({
  global: {
    useUTC: false
  }
});
stockInit(Highcharts)
boostInt(Highcharts)
export default {
  name: 'dataChart',
  props: {
    title: {
      type: String,
      default: ''
    },
    refreshTime: {
      type: Number,
      default: 5,
    },
    label: {
      type: String,
      default: ''
    },
    dataGroup: {
      type: Boolean,
      default: true,
    },
    multiple: {
      type: Boolean,
      default: false,
    },
  },
  components: {
    'highcharts': Chart,
  },
  data() {
    return {
      isActive: true, // 初始化为活动状态
      timer: null,
      refresh: true,
      avg_result: "-1",
      sum: 0,
      count: 0,
      chartOption: {
        rangeSelector: {
          buttons: [],
          inputEnabled: false,
        },
        chart: {
          zoomType: '',
          width: null,
          zooming: {
            mouseWheel: {
              enabled: false
            }
          },
        },
        navigator: {
          enabled: false
        },
        tooltip: {
          shared: true // 开启交叉显示多条曲线的数据
        },
        credits: {
          enabled: false
        },
        title: {
          text: this.title
        },
        // yAxis: {
        //   title: {
        //     text: this.label
        //   },
        //   opposite: false,
        // },
        exporting: {
          enabled: false
        },
        legend: false,
        plotOptions: {
          series: {}
        },
        series: [
          {
            name: this.title,
            type: "spline",
            data: [],
            tooltip: {
              pointFormat: '{point.series.name}:{point.y}'
            },
          }
        ]
      }
    }
  },
  methods: {
    clearData() {
      this.sum = 0;
      this.avg_result = "-1"
      this.count = 0
      for (let i in this.chartOption.series) {
        this.chartOption.series[i].data = []
      }
      clearInterval(this.timer)
    },
    redraw() {
      if (this.isActive) {
        this.$refs.chart.chart.redraw()
      }
    },
    resize() {
      this.$refs.chart.chart.setSize(null, null)
    },
    handleVisibilityChange() {
      // 当页面可见性状态发生变化时触发
      if (document.hidden) {
        this.isActive = false; // 页面不可见
      } else {
        this.isActive = true; // 页面可见
      }
    },
    addData(data) {
      let key = this.label.split(",")
      let title = this.title.split(",")
      if (key.length === 2) {
        this.chartOption.series.push(
            {
              name: this.title,
              type: "spline",
              data: [],
              tooltip: {
                pointFormat: '{point.series.name}:{point.y}'
              },
            }
        )
      }
      for (let i in key) {
        let value = parseFloat(data[key[i]])
        let time = (new Date()).getTime()
        this.chartOption.series[i].data.push([time, value])
        this.count += 1
        this.chartOption.series[i].name = title[i]
        this.sum += value
        this.avg_result = (this.sum / this.count).toFixed(2)
      }

    }
  },
  watch: {
    count: function () {
      if (this.count > 1) {
        if (this.timer === null) {
          this.timer = setInterval(this.redraw, this.refreshTime * 1000)
        }
      }
    },
    dataGroup: function (newVal) {
      if (newVal) {
        this.chartOption.plotOptions.series = {
          dataGrouping: {
            approximation: 'average',
            units: [[
              'minute',
              [1]
            ]]
          },
        }
      } else {
        this.chartOption.plotOptions.series = {}
      }
    }
  },
  mounted() {
    document.addEventListener('visibilitychange', this.handleVisibilityChange);

  }, beforeDestroy() {
    document.removeEventListener('visibilitychange', this.handleVisibilityChange);

    clearInterval(this.timer)
  }

}

</script>
<style scoped>

</style>