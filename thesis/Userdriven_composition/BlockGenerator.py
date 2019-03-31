#This file include All Block Generator Functions
from .models import *
import string
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect

#Random Name Generator
# This Function Will be Replaced With Watcherb
def FunctionNameGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#Main Execution Function
def BlockGenerator(nameid, service_type):
    BlockName = nameid
    BlockType = service_type
    BlockUiGenerator(BlockName,BlockType)
    BlockDeclaration(BlockName)
    BlockJsGenerator(BlockName,BlockType)
    BlockJsDeclaration(BlockName)

# This Function Genearte UI of The Block
def BlockUiGenerator(BlockName, BlockType):
    f= open("templetes/blocks.js","a+")
    BlockUiContainer = GetBlockUI(BlockName,BlockType)
    f.write(BlockUiContainer)
    f.close()

# This function Declare block to make it visible to End User
def BlockDeclaration(BlockName):
	f= open("templetes/blocks_declaration.html","a+")
	f.write('\n'+"<block type="+'"'+BlockName+'"'+"></block>")
	f.close()

#Generate JS file for show code 
def BlockJsGenerator(BlockName, BlockType):
    f= open("static/js/generators/codegenerator-"+BlockName+".js","w+")
    BlockJsContainer = GetBlockJs(BlockName,BlockType)
    f.write(BlockJsContainer)
    f.close()

#return Type of Block Ui you want
def GetBlockUI(BlockName, BlockType):
    if BlockType == 'sensor':
        BlockUi = '\n\n'+"//"+BlockName+" sensor block start"+'\n'+"Blockly.Blocks["+"'"+BlockName+"'"+"] = {"+'\n'+'\t'+"init: function() {"+'\n'+'\t\t'+"this.appendDummyInput()"+'\n'+'\t\t'+".appendField(new Blockly.FieldLabel("+"'"+BlockName+"'"+"));"+'\n'+'\t\t'+"this.setOutput(true, 'Number');"+'\n'+'\t\t'+"this.setColour(20);"+'\n'+'\t'+"}"+'\n'+"}"+'\n'+"//"+BlockName+" sensor block end"
        return BlockUi

#Greturn type of block js you want
def GetBlockJs(BlockName, BlockType):
    if BlockType == 'sensor':
        BlockJs = "Blockly.Python["+"'"+BlockName+"'"+"] = function(Block) {"+'\n'+'\t'+"var code = "+'"'+BlockName+'()"'+";"+'\n'+'\t'+"return [code, Blockly.Python.ORDER_ATOMIC];"+'\n'+"}"
        return BlockJs

def BlockJsDeclaration(BlockName):
    f= open("templetes/blocks_js_declaration.js","a+")
    f.write('\n\n<script src="static/js/generators/codegenerator-'+BlockName+'.js"></script>')
    f.close()