function support_popup(option, height, width, inner_html) {
  option['toolbox']['feature']['myFeature'] = {
    show: true,
    title: 'Open in new window',
    icon: 'image://http://127.0.0.1:5001/resources/popup_icon',
    onclick: function (){
      var win = window.open('template.html', '_blank', `height=${height}px, width=${width}px`);
      win.document.write(`${inner_html}`);
      win.document.close();
    }
  };
  return option;
};