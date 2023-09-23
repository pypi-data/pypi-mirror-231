function support_scientific_notation(option) {
  if (Array.isArray(option['yAxis'])) {
    for (var tar_ind = 0; tar_ind < option['yAxis'].length; tar_ind++) {
      if (option['yAxis'][tar_ind]['type'] === 'value') {
        option['yAxis'][tar_ind]['axisLabel']['formatter'] = function(val) {
          const superscripts = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹','¹⁰',
                    '¹¹', '¹²', '¹³', '¹⁴', '¹⁵', '¹⁶', '¹⁷', '¹⁸', '¹⁹','²⁰',
                    '²¹', '²²', '²³', '²⁴', '²⁵', '²⁶', '²⁷', '²⁸', '²⁹'];
          function toSuperscript(val) {
            if (val.toString().length > 6) {
              val = Number(val).toExponential().toString();
              if (val.includes('-')) {
                val = val.split('-');
                var val0 = val[0];
                var val1 = superscripts[val[1]];
                return val0 + '⁻' + val1
              }
              else if (val.includes('+')) {
                val = val.split('+');
                var val0 = val[0];
                var val1 = superscripts[val[1]];
                return val0 + '⁺' + val1
              }
            }
            else {
              return val
            }
          }
          return toSuperscript(val)
        }
      }
    }
  }
  else {
    if (option['yAxis']['type'] === 'value') {
      option['yAxis']['axisLabel']['formatter'] = function(val) {
        const superscripts = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹','¹⁰',
                '¹¹', '¹²', '¹³', '¹⁴', '¹⁵', '¹⁶', '¹⁷', '¹⁸', '¹⁹','²⁰',
                '²¹', '²²', '²³', '²⁴', '²⁵', '²⁶', '²⁷', '²⁸', '²⁹'];
        function toSuperscript(val) {
          if (val.toString().length > 6) {
            val = Number(val).toExponential().toString();
            if (val.includes('-')) {
              val = val.split('-');
              var val0 = val[0];
              var val1 = superscripts[val[1]];
              return val0 + '⁻' + val1
            }
            else if (val.includes('+')) {
              val = val.split('+');
              var val0 = val[0];
              var val1 = superscripts[val[1]];
              return val0 + '⁺' + val1
            }
          }
          else {
            return val
          }
        }
        return toSuperscript(val)
      }
    }
  };
  return option;
};

function custom_scatter_size(option) {
  
  for (var ind = 0; ind < option['series'].length; ind++) {
    if (option['series'][ind]['symbolSize'] === 'array_size') {
      var ind_ = option['series'][ind]['data_dict']['size']
      option['series'][ind]['symbolSize'] = function (data) {return data[ind_];}
    }
  }
  return option;
  
};

function show_scatter_label(option) {
  
  for (var ind = 0; ind < option['series'].length; ind++) {
    if (option['series'][ind]['label'] === 'show_label') {
      var ind_ = option['series'][ind]['data_dict']['label']
      option['series'][ind]['label'] = {
        show: true,
        formatter: function (params) {return params.data[ind_]; }
      }
    }
  }
  return option;
  
};

function custom_tooltip(option, dimension=2) {
  if (dimension === 2) {
    var xaxis_key = 'xAxis'
    var yaxis_key = 'yAxis'
  }

  else if (dimension === 3) {
    var xaxis_key = 'xAxis3D'
    var yaxis_key = 'yAxis3D'
    var zaxis_key = 'zAxis3D'
  }

  if (option['radar'] !== null) {
    var radar_names = []
    for (var ind_ = 0; ind_ < option['radar']['indicator'].length; ind_++) {
      radar_names.push(option['radar']['indicator'][ind_]['name']) 
    }
  }
  
  
  if (option[xaxis_key]['name'] !== null && option[xaxis_key]['name'] !== '' && Array.isArray(option[xaxis_key])!==true) {
    var xaxis_name = option[xaxis_key]['name'];
  }
  else {
    var xaxis_name = 'X';
  }

  if (option[yaxis_key]['name'] !== null && option[yaxis_key]['name'] !== ''&& Array.isArray(option[xaxis_key])!==true) {
    var yaxis_name = option[yaxis_key]['name'];
  }
  else {
    var yaxis_name = 'Y';
  }

  if (typeof zaxis_key !== 'undefined') {
    if (option[zaxis_key]['name'] !== ''&& Array.isArray(option[xaxis_key])!==true) {
      var zaxis_name = option[zaxis_key]['name'];
    }
    else {
      var zaxis_name = '';
    }
  }
  
  if (option['tooltip'] !== null) {
    option['tooltip']['formatter'] = function(params) {
      if (params.seriesName.includes('series')) {
        var series_name = ''
      }
      
      else {
        var series_name = params.seriesName + '<br>'
      }
  
      if (params.seriesType === 'scatter') {
        tooltip = series_name
            + xaxis_name + ': '+ Math.round(params.value[0] * 100) / 100
            +'<br>' + yaxis_name + ': ' + Math.round(params.value[1] * 100) / 100
      }
  
      else if (params.seriesType === 'scatter3D') {
        tooltip = series_name
            + xaxis_name + ': '+ Math.round(params.value[0] * 100) / 100
            +'<br>' + yaxis_name + ': ' + Math.round(params.value[1] * 100) / 100
            +'<br>' + zaxis_name + ': ' + Math.round(params.value[2] * 100) / 100
      }
      
      else if (params.seriesType === 'radar') {
        tooltip = params.name  + '<br>';
        for (var ind_ = 0; ind_ < option['radar']['indicator'].length; ind_++) {
          if (ind_ !== option['radar']['indicator'].length - 1) {
            tooltip += radar_names[ind_] + ': ' + Math.round(params.value[ind_] * 100) / 100 + '<br>'
          }
          else {
            tooltip += radar_names[ind_] + ': ' + Math.round(params.value[ind_] * 100) / 100
          }
          
        }
      }
      return tooltip;
    };
  }
  return option;
};

function support_brush_event(option) {
  if (option['event']['type_'] === 'brushselected') {
    if (option['event']['purpose'] === 'filter') {
      myChart.on(option['event']['type_'], (params) => {
        var brushed = [];
        function range(start, end) {
          var ans = [];
          for (let i = start; i < end; i++) {
              ans.push(i);
          }
          return ans;
        }
        var data = option['event']['initial_data_target'];
        var data_all = data[0].concat(data[1]);
        
        var all_idx = range(0, data_all.length);
        var data_source_ind = option['event']['data_source'];
        var brushComponent = params.batch[0];
        for (var sIdx = 0; sIdx < brushComponent.selected.length; sIdx++) {
          var rawIndices = brushComponent.selected[sIdx].dataIndex;
          brushed.push(rawIndices);
        }
        var brushed_all = brushed[0].concat(brushed[1].map(x => x + data[0].length));
        var unselected = all_idx.filter(function(x) {
          return brushed_all.indexOf(x) < 0;
        });
        //new histogram                          
      myChart.setOption(option);
      })
    }
  }
  return option;
};
var select_legend
function support_click_event(option) {
  if (option['event']['type_'] === 'click') {
    if (option['event']['purpose'] === 'filter') {
      if (option['link_id'] === null) {
        var link_id = option['echarts_id'];
      }
      else {
        var link_id = option['link_id'];
      }
      var dom = document.getElementById(link_id);
      var bind_chart = echarts.init(dom, null, {
          renderer: 'canvas',
          useDirtyRect: false
      });

      bind_chart.on('legendselectchanged', function (params) {
        select_legend = params.selected;
      });

      bind_chart.on(option['event']['type_'], (params) => {
        if (option['event']['plot_type'] === 'scatter') {
          var selected = params.seriesName;
          change_select_sctter(bind_chart, option, selected, select_legend);
        }

        else if (option['event']['plot_type'] === 'bar') {
          var selected = params.name;
          var selected_index = params.dataIndex;
          change_select_bar(bind_chart, option, selected, selected_index);
        }       
      });
      
    }
  }
  return option;
};

function change_select_bar(bind_chart, option, selected, selected_index) {
  
  for (var ind = 0; ind < option['series'].length; ind++) {
    var tmp = option['series'][ind];
    if (tmp['type'] === 'bar') {
      for (var ind_2 = 0; ind_2 < tmp['data'].length; ind_2++) {
        if (tmp['data'][ind_2]['itemStyle']['color'] !== '#5470c6b3') {
          tmp['data'][ind_2]['itemStyle']['color'] = '#5470c6b3'
        }
      }
      tmp['data'][selected_index]['itemStyle']['color'] = 'red'
    }
    option['series'][ind] = tmp;
  }

  var plot_option = Object.assign({}, option);
  bind_chart.setOption(plot_option);

  var content = {'selected_name': selected,
                //  'selected_id': selected_index,
                 'link_ids': option['event']['target_ids']}

  let testRequest = new Request(option['event']['router_url'], {
      method: 'post',
      headers: {
          'Content-Type': 'application/json;charset=utf-8;',
          'Access-Control-Allow-Origin':'*',
          'Access-Control-Allow-Credentials': 'true',
          'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'
      },
      body: JSON.stringify(content)
  });
  var dom_dict = {}
  fetch(testRequest).then(response => {
      let result = response.json();
      result.then(res => {
        for (single_plot of res) {
          dom_dict[single_plot['link_id']] = document.getElementById(single_plot['link_id']);
          setInnerHTML(dom_dict[single_plot['link_id']], single_plot['html']);
        };
      });
  });
}

function change_select_sctter(bind_chart, option, selected, select_legend) {
  if (option['event']['additional_info'] !== null) {
    var selected_ind = option['event']['additional_info']['n_top_inverse'][selected];
    var selected_neighbour = option['event']['additional_info']['n_top'][selected_ind]['n_top_name'];
    var with_link = option['event']['additional_info']['with_link'];

    //clear lines
    var remove_lines = [];
    var link_point = [];
    for (var ind = 0; ind < option['series'].length; ind++) {
      var tmp = option['series'][ind];
      if (tmp['type'] === 'line') {
        remove_lines.push(ind)
      }
    }
    for (let i = remove_lines.length - 1; i >= 0; i--) {
      option['series'].splice(remove_lines[i], 1);
    }
  }
  else {
    var selected_neighbour = null
  }

  for (var ind = 0; ind < option['series'].length; ind++) {
    var tmp = option['series'][ind];
    if (tmp['type'] === 'radar') {
      for (var ind_2 = 0; ind_2 < tmp['data'].length; ind_2++) {
        if (tmp['data'][ind_2]['name'] !== selected) {
          if (tmp['data'][ind_2]['lineStyle']['color'].length < 9) {
            tmp['data'][ind_2]['lineStyle']['color'] = tmp['data'][ind_2]['lineStyle']['color']+'80';
          }
        }
        else if (tmp['data'][ind_2]['name'] === selected) {
          if (tmp['data'][ind_2]['lineStyle']['color'].length === 9) {
            tmp['data'][ind_2]['lineStyle']['color'] = tmp['data'][ind_2]['lineStyle']['color'].slice(0, -2);
          }
        }
      }
    }
    else if (tmp['type'] === 'scatter') {
      if (tmp['is_text'] === false) {
        if (selected_neighbour.includes(tmp['name'])) {
          link_point.push(tmp['data'][0])
        }
        if (tmp['name'] !== selected) {
          if (tmp['color'].length < 9) {
            tmp['color'] = tmp['color']+'80';
          }
        }
        else if (tmp['name'] === selected) {
          var origin_point = tmp['data']
          if (tmp['color'].length === 9) {
            tmp['color'] = tmp['color'].slice(0, -2);
          }
        }
      }
      else {
        if (tmp['name'] !== selected) {
          if (tmp['data'][0]['label']['color'].length < 9) {
            tmp['data'][0]['label']['color'] = tmp['data'][0]['label']['color']+'80';
          }
        }
        else if (tmp['name'] === selected) {
          var origin_point = tmp['data']
          if (tmp['data'][0]['label']['color'].length === 9) {
            tmp['data'][0]['label']['color'] = tmp['data'][0]['label']['color'].slice(0, -2);
          }
        }
      }
    }
    option['series'][ind] = tmp;
  }

  if (with_link === true) {
    if (selected_neighbour !== null) {
      for (var ind = 0; ind < link_point.length; ind++) {
        option['series'].push(
          {
            type:'line',
            data: [origin_point[0], link_point[ind]],
            color:'black',
            symbol:'none',
            lineStyle: {width:1},
          }
        )
      }
    }
  }
  if (option['legend'] !== null) {
    option['legend']['selected'] = select_legend;
  }
  
  var plot_option = Object.assign({}, option);
  bind_chart.setOption(plot_option);

  var content = {'selected_name': selected,
                //  'selected_id': selected_index,
                 'link_ids': option['event']['target_ids']}

  let testRequest = new Request(option['event']['router_url'], {
      method: 'post',
      headers: {
          'Content-Type': 'application/json;charset=utf-8;',
          'Access-Control-Allow-Origin':'*',
          'Access-Control-Allow-Credentials': 'true',
          'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'
      },
      body: JSON.stringify(content)
  });
  var dom_dict = {}
  fetch(testRequest).then(response => {
      let result = response.json();
      result.then(res => {
        for (single_plot of res) {
          dom_dict[single_plot['link_id']] = document.getElementById(single_plot['link_id']);
          setInnerHTML(dom_dict[single_plot['link_id']], single_plot['html']);
        };
      });
  });
};