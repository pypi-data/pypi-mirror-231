var layerLoadErrorMessages=[];showMessage('Loading',staticTemplates.loadingModal[mode]);
function runGeeViz(){
try{
	Map2.addSerializedLayer({"result": "0", "values": {"0": {"functionInvocationValue": {"functionName": "Image.select", "arguments": {"bandSelectors": {"constantValue": ["landcover"]}, "input": {"functionInvocationValue": {"functionName": "Image.load", "arguments": {"id": {"constantValue": "USGS/NLCD_RELEASES/2016_REL/2011"}}}}}}}}},{"autoViz": true},'NLCD 2011 Landcover/Landuse',false);
}catch(err){
	layerLoadErrorMessages.push("Error loading: NLCD 2011 Landcover/Landuse<br>GEE "+err);}
try{
	Map2.addSerializedLayer({"result": "0", "values": {"2": {"constantValue": "landcover"}, "1": {"functionInvocationValue": {"functionName": "Image.select", "arguments": {"bandSelectors": {"arrayValue": {"values": [{"valueReference": "2"}]}}, "input": {"argumentReference": "_MAPPING_VAR_0_0"}}}}, "4": {"constantValue": "bns"}, "3": {"functionInvocationValue": {"functionName": "Element.set", "arguments": {"key": {"valueReference": "4"}, "object": {"argumentReference": "_MAPPING_VAR_0_0"}, "value": {"functionInvocationValue": {"functionName": "Image.bandNames", "arguments": {"image": {"argumentReference": "_MAPPING_VAR_0_0"}}}}}}}, "0": {"functionInvocationValue": {"functionName": "Collection.limit", "arguments": {"collection": {"functionInvocationValue": {"functionName": "Collection.map", "arguments": {"baseAlgorithm": {"functionDefinitionValue": {"argumentNames": ["_MAPPING_VAR_0_0"], "body": "1"}}, "collection": {"functionInvocationValue": {"functionName": "Collection.filter", "arguments": {"collection": {"functionInvocationValue": {"functionName": "Collection.map", "arguments": {"baseAlgorithm": {"functionDefinitionValue": {"argumentNames": ["_MAPPING_VAR_0_0"], "body": "3"}}, "collection": {"functionInvocationValue": {"functionName": "Collection.filter", "arguments": {"collection": {"functionInvocationValue": {"functionName": "ImageCollection.load", "arguments": {"id": {"constantValue": "USGS/NLCD_RELEASES/2016_REL"}}}}, "filter": {"functionInvocationValue": {"functionName": "Filter.calendarRange", "arguments": {"end": {"constantValue": 2020}, "field": {"constantValue": "year"}, "start": {"constantValue": 2000}}}}}}}}}}, "filter": {"functionInvocationValue": {"functionName": "Filter.listContains", "arguments": {"leftField": {"valueReference": "4"}, "rightValue": {"valueReference": "2"}}}}}}}}}}, "key": {"constantValue": "system:time_start"}}}}}},{"autoViz": true},'NLCD Landcover/Landuse Time Series',false);
}catch(err){
	layerLoadErrorMessages.push("Error loading: NLCD Landcover/Landuse Time Series<br>GEE "+err);}
try{
	Map2.addSerializedLayer({"result": "0", "values": {"0": {"functionInvocationValue": {"functionName": "Image.select", "arguments": {"bandSelectors": {"constantValue": ["percent_tree_cover"]}, "input": {"functionInvocationValue": {"functionName": "Image.load", "arguments": {"id": {"constantValue": "USGS/NLCD_RELEASES/2016_REL/2016"}}}}}}}}},{"min": 20, "max": 80, "palette": "555,0A0"},'NLCD 2016 TCC',false);
}catch(err){
	layerLoadErrorMessages.push("Error loading: NLCD 2016 TCC<br>GEE "+err);}
try{
	Map2.addSerializedLayer({"result": "0", "values": {"1": {"functionInvocationValue": {"functionName": "Image.byte", "arguments": {"value": {"functionInvocationValue": {"functionName": "Image.select", "arguments": {"bandSelectors": {"constantValue": [0]}, "input": {"functionInvocationValue": {"functionName": "Image.updateMask", "arguments": {"image": {"argumentReference": "_MAPPING_VAR_0_0"}, "mask": {"functionInvocationValue": {"functionName": "Image.neq", "arguments": {"image1": {"argumentReference": "_MAPPING_VAR_0_0"}, "image2": {"functionInvocationValue": {"functionName": "Image.constant", "arguments": {"value": {"constantValue": 0}}}}}}}}}}, "newNames": {"constantValue": ["Burn Severity"]}}}}}}}, "0": {"functionInvocationValue": {"functionName": "reduce.max", "arguments": {"collection": {"functionInvocationValue": {"functionName": "Collection.map", "arguments": {"baseAlgorithm": {"functionDefinitionValue": {"argumentNames": ["_MAPPING_VAR_0_0"], "body": "1"}}, "collection": {"functionInvocationValue": {"functionName": "ImageCollection.load", "arguments": {"id": {"constantValue": "projects/gtac-mtbs/assets/burn_severity_mosaics/MTBS"}}}}}}}}}}}},{"min": 1, "max": 6, "palette": ["006400", "7fffd4", "ffff00", "ff0000", "7fff00", "ffffff"], "classLegendDict": {"1 Unburned to Low": "006400", "2 Low": "7fffd4", "3 Moderate": "ffff00", "4 High": "ff0000", "5 Increased Greenness": "7fff00", "6 Non-Processing Area Mask": "ffffff"}, "queryDict": {"1": "Unburned to Low", "2": "Low", "3": "Moderate", "4": "High", "5": "Increased Greenness", "6": "Non-Processing Area Mask"}},'MTBS 1984-2017 Highest Severity',true);
}catch(err){
	layerLoadErrorMessages.push("Error loading: MTBS 1984-2017 Highest Severity<br>GEE "+err);}
try{
	Map2.addSerializedLayer({"result": "0", "values": {"0": {"functionInvocationValue": {"functionName": "Collection.loadTable", "arguments": {"tableId": {"constantValue": "projects/gtac-mtbs/assets/perimeters/mtbs_perims_DD"}}}}}},{"strokeColor": "00F"},'MTBS Burn Perimeters',true);
}catch(err){
	layerLoadErrorMessages.push("Error loading: MTBS Burn Perimeters<br>GEE "+err);}
try{
	Map2.addSerializedLayer({"result": "0", "values": {"0": {"functionInvocationValue": {"functionName": "Collection.filter", "arguments": {"collection": {"functionInvocationValue": {"functionName": "Collection.loadTable", "arguments": {"tableId": {"constantValue": "projects/USFS/LCMS-NFS/CONUS-Ancillary-Data/NPS_Boundaries"}}}}, "filter": {"functionInvocationValue": {"functionName": "Filter.equals", "arguments": {"leftField": {"constantValue": "PARKNAME"}, "rightValue": {"constantValue": "Yellowstone"}}}}}}}}},{"layerType": "geeVector"},'Yellowstone National Park',true);
}catch(err){
	layerLoadErrorMessages.push("Error loading: Yellowstone National Park<br>GEE "+err);}
try{
	Map2.addSerializedLayer({"result": "0", "values": {"0": {"functionInvocationValue": {"functionName": "ImageCollection.load", "arguments": {"id": {"constantValue": "JRC/GSW1_0/YearlyHistory"}}}}}},{"min": 1, "max": 3, "palette": ["ffffff", "99d9ea", "0000ff"], "classLegendDict": {"1 Not Water": "ffffff", "2 Seasonal Water": "99d9ea", "3 Permanent Water": "0000ff"}, "queryDict": {"1": "1 Not Water", "2": "2 Seasonal Water", "3": "3 Permanent Water"}},'JRC Surface Water Time Series',false);
}catch(err){
	layerLoadErrorMessages.push("Error loading: JRC Surface Water Time Series<br>GEE "+err);}
try{
	Map2.addSerializedLayer({"result": "0", "values": {"0": {"functionInvocationValue": {"functionName": "reduce.mode", "arguments": {"collection": {"functionInvocationValue": {"functionName": "ImageCollection.load", "arguments": {"id": {"constantValue": "JRC/GSW1_0/YearlyHistory"}}}}}}}}},{"min": 1, "max": 3, "palette": ["ffffff", "99d9ea", "0000ff"], "classLegendDict": {"1 Not Water": "ffffff", "2 Seasonal Water": "99d9ea", "3 Permanent Water": "0000ff"}, "queryDict": {"1": "1 Not Water", "2": "2 Seasonal Water", "3": "3 Permanent Water"}},'JRC Surface Water Mode',false);
}catch(err){
	layerLoadErrorMessages.push("Error loading: JRC Surface Water Mode<br>GEE "+err);}
try{
	Map2.addSerializedTimeLapse({"result": "0", "values": {"0": {"functionInvocationValue": {"functionName": "ImageCollection.load", "arguments": {"id": {"constantValue": "JRC/GSW1_0/YearlyHistory"}}}}}},{"min": 1, "max": 3, "palette": ["ffffff", "99d9ea", "0000ff"], "classLegendDict": {"1 Not Water": "ffffff", "2 Seasonal Water": "99d9ea", "3 Permanent Water": "0000ff"}, "queryDict": {"1": "1 Not Water", "2": "2 Seasonal Water", "3": "3 Permanent Water"}},'JRC Surface Water Time Lapse',false);
}catch(err){
	layerLoadErrorMessages.push("Error loading: JRC Surface Water Time Lapse<br>GEE "+err);}
if(layerLoadErrorMessages.length>0){showMessage("Map.addLayer Error List",layerLoadErrorMessages.join("<br>"));}
setTimeout(function(){if(layerLoadErrorMessages.length===0){$('#close-modal-button').click();}}, 2500);
synchronousCenterObject({"geodesic": false, "type": "Polygon", "coordinates": [[[-111.15597830230226, 44.132436299453055], [-109.82420136249235, 44.132436299453055], [-109.82420136249235, 45.10896200948672], [-111.15597830230226, 45.10896200948672], [-111.15597830230226, 44.132436299453055]]]})
yLabelBreakLength = 2
yLabelMaxLength = 5
$('#query-label').click();
queryWindowMode = "sidePane"
}