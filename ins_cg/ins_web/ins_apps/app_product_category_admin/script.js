ins(".-title-input")._on("keyup", (o, e) => {
    var value = o._getValue().trim().toLowerCase().replace(/\s+/g, "_");
    ins(".-alias-input")._setValue(value);

});