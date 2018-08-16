#include <string.h>
#include "XPLMPlugin.h"

#ifndef XPLM300
	#error This is made to be compiled against the XPLM300 SDK
#endif

PLUGIN_API int XPluginStart(
							char *		outName,
							char *		outSig,
							char *		outDesc)
{
	strcpy(outName, "HelloWorld3Plugin");
	strcpy(outSig, "xpsdk.examples.helloworld3plugin");
	strcpy(outDesc, "A Hello World plug-in for the XPLM300 SDK.");
	return 1;
}

PLUGIN_API void	XPluginStop(void)
{
}

PLUGIN_API void XPluginDisable(void) { }
PLUGIN_API int  XPluginEnable(void)  { return 1; }
PLUGIN_API void XPluginReceiveMessage(XPLMPluginID inFrom, int inMsg, void * inParam) { }