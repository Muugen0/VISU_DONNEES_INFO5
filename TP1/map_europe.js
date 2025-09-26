const map = eurostatmap
                .map('choropleth')
                .title('Self-reported consultation of mental healthcare')
                .width(1080)
                .subtitle('2014')
                .stat({eurostatDatasetCode: 'hlth_ehis_am6e', unitText: '%', filters:{TIME: '2014', sex: 'T', isco08: 'OC2634_2212PSY'  }})
                .legend({ x: 10, y: 200, title: 'Percentage of consultations, %', boxOpacity: 0 })
                .numberOfClasses(6)
                .colors(['#E97452', '#D65D42', '#C34632', '#B12E21', '#9E1711', '#8B0001'])
                .nutsLevel(0)
                .build()





document.getElementById("2014_button").addEventListener("click", function() {
    const map = eurostatmap
                .map('choropleth')
                .title('Self-reported consultation of mental healthcare')
                .width(1080)
                .subtitle('2014')
                .stat({eurostatDatasetCode: 'hlth_ehis_am6e', unitText: '%', filters:{TIME: '2014', sex: 'T', isco08: 'OC2634_2212PSY'  }})
                .legend({ x: 10, y: 200, title: 'Percentage of consultations, %', boxOpacity: 0 })
                .numberOfClasses(6)
                .colors(['#E97452', '#D65D42', '#C34632', '#B12E21', '#9E1711', '#8B0001'])
                .nutsLevel(0)
                .build()
});

document.getElementById("2019_button").addEventListener("click", function() {
    const map = eurostatmap
                .map('choropleth')
                .title('Self-reported consultation of mental healthcare')
                .width(1080)
                .subtitle('2019')
                .stat({eurostatDatasetCode: 'hlth_ehis_am6e', unitText: '%', filters:{TIME: '2019', sex: 'T', isco08: 'OC2634_2212PSY'  }})
                .legend({ x: 10, y: 200, title: 'Percentage of consultations, %', boxOpacity: 0 })
                .numberOfClasses(6)
                .colors(['#E97452', '#D65D42', '#C34632', '#B12E21', '#9E1711', '#8B0001'])
                .nutsLevel(0)
                .build()
});
