window.onload = function () {
    let chartCpuDom = document.getElementById('chartCpuDom');
    let chartMemDom = document.getElementById('chartMemDom');
    let chartNetDom = document.getElementById('chartNetDom');
    let chartDiskDom = document.getElementById('chartDiskDom');

    genChart();
    setInterval(genChart, 60000);

    function genChart() {
        $.ajax({
            url: '/api/get-server-resource/',
            type: 'GET',

            success: (result) => {
                showCharts(result);
            },
            error: (err) => {
                console.error(err);
            }
        });
    }


    function showCharts(resource) {
        let resourceList = resource.server_resource;

        showCpuCharts(resourceList);
        showMemCharts(resourceList);
        showNetCharts(resourceList);
        showDiskCharts(resourceList);
    }

    function showCpuCharts(resourceList) {
        let xAxis = [], yAxis = [];
        for (let i in resourceList) {
            let jsonData = JSON.parse(resourceList[i]);
            xAxis.unshift(jsonData.simple_time);
            yAxis.unshift(jsonData.cpu);
        }
        let option = {
            title: [
                {
                    text: 'CPU资源监视',
                    textStyle: {
                        color: '#525252',
                        fontWeight: 'normal',
                        fontSize: 14
                    },

                },
                {
                    subtext: `当前cpu占用：${yAxis[yAxis.length - 1]}%`,
                    left: 'right',
                }
            ],
            grid: {
                top: '18%',
            },
            xAxis: {
                type: 'category',
                data: xAxis,
            },
            yAxis: {
                type: 'value',
            },
            tooltip: {
                trigger: 'axis',
                formatter: '{b}<br/>CPU占用：{c}%',
            },
            series: [
                {
                    data: yAxis,
                    type: 'line',
                    symbol: 'none'
                }
            ]
        }

        let chartCpu = echarts.init(chartCpuDom);
        chartCpu.setOption(option);
    }

    function showMemCharts(resourceList) {
        let xAxis = [], yAxis = [];
        for (let i in resourceList) {
            let jsonData = JSON.parse(resourceList[i]);
            xAxis.unshift(jsonData.simple_time);
            yAxis.unshift(jsonData.memory);
        }
        let option = {
            title: [
                {
                    text: '内存监视',
                    textStyle: {
                        color: '#525252',
                        fontWeight: 'normal',
                        fontSize: 14
                    },
                },
                {
                    subtext: `当前内存占用：${yAxis[yAxis.length - 1]}%`,
                    left: 'right',
                }
            ],
            grid: {
                top: '18%',
            },
            xAxis: {
                type: 'category',
                data: xAxis,
            },
            yAxis: {
                type: 'value',
            },
            tooltip: {
                trigger: 'axis',
                formatter: '{b}<br/>内存占用：{c}%',
            },
            series: [
                {
                    data: yAxis,
                    type: 'line',
                    symbol: 'none'
                }
            ]
        }

        let chartMem = echarts.init(chartMemDom);
        chartMem.setOption(option);
    }

    function showNetCharts(resourceList) {
        // 网络io的单位是 Mbps
        let xAxis = [], yAxisSent = [], yAxisRecv = [];
        for (let i in resourceList) {
            let jsonData = JSON.parse(resourceList[i]);
            xAxis.unshift(jsonData.simple_time);
            yAxisSent.unshift(jsonData.net_io_sent);
            yAxisRecv.unshift(jsonData.net_io_recv);
        }
        let option = {
            title: {
                text: '带宽IO(Mbps)',
                textStyle: {
                    color: '#525252',
                    fontWeight: 'normal',
                    fontSize: 14
                },
            },
            grid: {
                top: '18%',
            },
            xAxis: {
                type: 'category',
                data: xAxis,
            },
            yAxis: {
                type: 'value',
            },
            tooltip: {
                trigger: 'axis',
                formatter: '{b}<br/>出：{c0}Mbps<br/>入：{c1}Mbps',
            },
            legend: {
                data: ['出', '入']
            },
            series: [
                {
                    name: '出',
                    data: yAxisSent,
                    type: 'line',
                    symbol: 'none',
                    stack: 'Total'
                },
                {
                    name: '入',
                    data: yAxisRecv,
                    type: 'line',
                    symbol: 'none',
                    stack: 'Total'
                }
            ]
        }

        let chartNet = echarts.init(chartNetDom);
        chartNet.setOption(option);
    }

    function showDiskCharts(resourceList) {
        let xAxis = [], yAxisRead = [], yAxisWrite = [];
        for (let i in resourceList) {
            let jsonData = JSON.parse(resourceList[i]);
            xAxis.unshift(jsonData.simple_time);
            yAxisRead.unshift(jsonData.disk_io_read);
            yAxisWrite.unshift(jsonData.disk_io_write);
        }
        console.log(yAxisRead)
        console.log(yAxisWrite)
        let option = {
            title: {
                text: '磁盘IO(KB/s)',
                textStyle: {
                    color: '#525252',
                    fontWeight: 'normal',
                    fontSize: 14
                },
            },
            grid: {
                top: '18%',
            },
            xAxis: {
                type: 'category',
                data: xAxis,
            },
            yAxis: {
                type: 'value',
            },
            tooltip: {
                trigger: 'axis',
                formatter: '{b}<br/>读：{c0}KB/s<br/>写：{c1}KB/s',
            },
            legend: {
                data: ['读', '写']
            },
            series: [
                {
                    name: '读',
                    data: yAxisRead,
                    type: 'line',
                    symbol: 'none',
                    stack: 'Total'
                },
                {
                    name: '写',
                    data: yAxisWrite,
                    type: 'line',
                    symbol: 'none',
                    stack: 'Total'
                }
            ]
        }

        let chartDisk = echarts.init(chartDiskDom);
        chartDisk.setOption(option);
    }
}