var agent = window.navigator.userAgent;
var IExplorer = agent.indexOf('MSIE');
var IE11 = agent.indexOf('Trident/');
if(IExplorer>=0 || IE11>=0){
	location.href = 'unsupported';
}
