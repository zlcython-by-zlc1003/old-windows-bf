Blockly.defineBlocksWithJsonArray([
    {
        "type": "SayHello",
        "message0": "Say hello",
        "previousStatement": null,
        "nextStatement": null,
        "colour": 355
    },
    {
        "type": "printtext",
        "message0": "print text %1",
        "args0": [
            {
                "type": "field_input",
                "name": "VALUE"
            }
        ],
        "previousStatement": null,
        "nextStatement": null,
        "colour": 355
    }
]);

Blockly.Python['SayHello'] = function (block) {
    return 'print("Hello World")\n';
};

Blockly.inject('codediv', {
    toolbox: document.getElementById('toolbox'),
    scrollbars: false
})
Blockly.Python['printtext'] = function (block) {
    let value = '\'' + block.getFieldValue('VALUE') + '\'';
    return 'print(' + value + ');\n';
};

function updateCode() {
    var code = Blockly.Python.workspaceToCode(Blockly.getMainWorkspace());
    document.getElementById('code').innerHTML = code;
}

document.getElementById('btn1').addEventListener('click', function () {
    updateCode();
});