function add_controler(option) {

  var div_id = option['controler_data']['div_id'];
  var schema = option['controler_data']['schema'];
  var configParameters = option['controler_data']['config'];
  var folder = option['controler_data']['folder'];
  var label = option['controler_data']['label'];

  var DEFAULT_PALETTE = ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc']

  var fieldIndices = schema.reduce(function (obj, item) {
    obj[item.name] = item.index;
    return obj;
  }, {});

  app.config = {};
  for (var ind = 0; ind < Object.keys(configParameters).length; ind++) {
    var attribute_name = Object.keys(configParameters)[ind];
    app.config[attribute_name] = configParameters[attribute_name]['default']
  }
  
  const url = 'http://127.0.0.1:5001';
  var data;
  async function data_update() {

    //if (labels.length == 1) {
    //  labels = labels[0]
    //}

    var content = {'sample_method': app.config.Method,
                   'sample_max_size': app.config.MaxNum,
                   'label': label};
    
    
    let testRequest = new Request(url + '/function/get_sampled_data', {
      method: 'post',
      headers: {
        'Content-Type': 'application/json;charset=utf-8;',
        'Access-Control-Allow-Origin':'http://127.0.0.1:8888',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'
      },
      body: JSON.stringify(content)
    });
    await fetch(testRequest).then(async response => {
      let result = await response.json();
      data = result['sampled_data'];
    });

    series = []
    for (var ind = 0; ind < data.length; ind++) {
      series.push({
        dimensions: [app.config.xAxis3D, app.config.yAxis3D, app.config.yAxis3D],
        itemStyle: {opacity: app.config.opacity},
        // symbol: app.config.symbol,
        symbolSize: app.config.symbolSize,
        color: DEFAULT_PALETTE[ind],
        data: data[ind].map(function (item, idx) {
          return [
            item[fieldIndices[app.config.xAxis3D]],
            item[fieldIndices[app.config.yAxis3D]],
            item[fieldIndices[app.config.zAxis3D]],
            idx
          ];
        })
      });
    }

    myChart.setOption({
      xAxis3D: {
        name: app.config.xAxis3D
      },
      yAxis3D: {
        name: app.config.yAxis3D
      },
      zAxis3D: {
        name: app.config.zAxis3D
      },
      series: series
    });
  };

  app.config['onDataChange'] = data_update
  data_update()

  
  app.config['onChange'] = function () {

    series = []
    for (var ind = 0; ind < data.length; ind++) {
      series.push({
        dimensions: [app.config.xAxis3D, app.config.yAxis3D, app.config.yAxis3D],
        // symbol: app.config.symbol,
        itemStyle: {opacity: app.config.opacity},
        symbolSize: app.config.symbolSize,
        color: DEFAULT_PALETTE[ind],
        data: data[ind].map(function (item, idx) {
          return [
            item[fieldIndices[app.config.xAxis3D]],
            item[fieldIndices[app.config.yAxis3D]],
            item[fieldIndices[app.config.zAxis3D]],
            idx
          ];
        })
      });
    };
  
    myChart.setOption({
      xAxis3D: {
        name: app.config.xAxis3D
      },
      yAxis3D: {
        name: app.config.yAxis3D
      },
      zAxis3D: {
        name: app.config.zAxis3D
      },
      series: series
    });
  };
  
  app.configParameters = configParameters;
  if (div_id !== null) {
    var datgui = new dat.GUI({ name: 'settings', autoPlace: false, width: '25%', closeOnTop: true});
  }
  else {
    var datgui = new dat.GUI({ name: 'settings', autoPlace: true, width: '25%', closeOnTop: true});
  }

  var folder_dict = {'': datgui}; 
  for (folder_name of Object.keys(folder)){
    folder_dict[folder_name] = datgui.addFolder(folder_name)
    folder_dict[folder_name].open()
  }

	let dom_dat_outer = document.getElementsByClassName('dg ac');
  let dom_dat = document.getElementsByClassName('dg main a');
	// let pos = dom.getBoundingClientRect();
	dom_dat_outer[0].style.top = '5%';
	dom_dat[0].style.width = '25%';
  
	//dom_dat[0].style.left = pos.left + 'px';

  for (let key of Object.keys(app.configParameters)) {
    const param = app.configParameters[key]

    if (param.folder == 'Sampler') {
      if ("min" in param) {
        folder_dict[param.folder].add(app.config, key).min(param.min).max(param.max).step(1).name(param.display_name).onChange(app.config.onDataChange);
      } else if ("options" in param) {
        folder_dict[param.folder].add(app.config, key, param.options).name(param.display_name).onChange(app.config.onDataChange);
      }
    }

    else if (key === 'opacity') {
      folder_dict[param.folder].add(app.config, key).min(param.min).max(param.max).step(0.1).name(param.display_name).onChange(app.config.onChange);
    }

    else {
      if ("min" in param) {
        folder_dict[param.folder].add(app.config, key).min(param.min).max(param.max).step(1).name(param.display_name).onChange(app.config.onChange);
      } else if ("options" in param) {
        folder_dict[param.folder].add(app.config, key, param.options).name(param.display_name).onChange(app.config.onChange);
      }
    }
  }

  if (div_id !== null) {
    const containerEl = document.getElementById(div_id)
    containerEl.appendChild(gui.domElement);
  }
  
  return datgui;
};