
{
	"job1" :
	{
		"baseroot" : "~/work/aibpublisher/static/additback/",
		"jsroot" : "vendor/",
		"cssroot" : "./",
		"outroot" : "./",

		"chores" :
		{
			"vendor_packed.js" : ["jquery-1.7.1.min.js","jquery.tipsy.js","mustache.js"]
		}
	},
	"job2" :
	{
		"baseroot" : "~/work/aibpublisher/static/additback/",
		"jsroot" : "base/",
		"cssroot" : "./",
		"outroot" : "./",

		"chores" :
		{
			"aib.base.min.js" : ["base.js", "additback.boot.js", "additback.base64.js"]
		}
	}
}
