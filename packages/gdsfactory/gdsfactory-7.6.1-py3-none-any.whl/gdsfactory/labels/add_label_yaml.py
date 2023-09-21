"""Add label YAML."""
from __future__ import annotations

import json
from functools import partial
from typing import Any

import pydantic
from omegaconf import OmegaConf

import gdsfactory as gf
from gdsfactory.read.from_yaml import valid_anchor_point_keywords
from gdsfactory.typings import LayerSpec


@pydantic.validate_call
def add_label_yaml(
    component: gf.Component,
    layer: LayerSpec = "LABEL",
    measurement: str | None = None,
    measurement_settings: dict[str, Any] | None = None,
    analysis: str | None = None,
    analysis_settings: dict[str, Any] | None = None,
    doe: str | None = None,
    with_yaml_format: bool = True,
    anchor: str = "sw",
) -> gf.Component:
    """Returns Component with measurement label.

    Args:
        component: to add labels to.
        layer: text label layer.
        measurement: measurement config name.
        measurement_settings: measurement settings.
        analysis: analysis name.
        analysis_settings: Extra analysis settings. Defaults to component settings.
        doe: Design of Experiment name.
        with_yaml_format: whether to use yaml or json format.
        anchor: anchor point for the label. Defaults to south-west "sw". \
            Valid options are: "n", "s", "e", "w", "ne", "nw", "se", "sw", "c".
    """
    from gdsfactory.pdk import get_layer

    layer = get_layer(layer)
    analysis_settings = analysis_settings or {}
    measurement_settings = measurement_settings or {}
    analysis_settings.update(component.metadata.get("full", {}))

    optical_ports = component.get_ports_list(port_type="optical")
    electrical_ports = component.get_ports_list(port_type="electrical")

    if anchor not in valid_anchor_point_keywords:
        raise ValueError(f"anchor {anchor} not in {valid_anchor_point_keywords}. ")

    xc, yc = getattr(component.size_info, anchor)

    d = dict(
        name=component.name,
        doe=doe,
        measurement=measurement,
        analysis=analysis,
        measurement_settings=measurement_settings,
        analysis_settings=analysis_settings,
        xopt=[int(optical_ports[0].x - xc)] if optical_ports else [],
        yopt=[int(optical_ports[0].y - yc)] if optical_ports else [],
        xelec=[int(electrical_ports[0].x - xc)] if electrical_ports else [],
        yelec=[int(electrical_ports[0].y - yc)] if electrical_ports else [],
    )
    text = OmegaConf.to_yaml(d) if with_yaml_format else json.dumps(d)
    label = gf.Label(
        text=text,
        origin=(xc, yc),
        anchor="o",
        layer=layer[0],
        texttype=layer[1],
    )
    component.add(label)
    return component


add_label_json = partial(add_label_yaml, with_yaml_format=False)


if __name__ == "__main__":
    import yaml

    measurement_settings = dict(
        wavelenth_min=1550, wavelenth_max=1570, wavelength_steps=10
    )
    with_yaml_format = False
    with_yaml_format = True

    add_label_yaml_cutback_loopback4 = partial(
        add_label_yaml,
        measurement_settings=measurement_settings,
        with_yaml_format=with_yaml_format,
        anchor="sw",
    )

    c = gf.c.straight(length=11)
    c = gf.c.mmi2x2(length_mmi=2.2)
    c = gf.routing.add_fiber_array(
        c,
        get_input_labels_function=None,
        grating_coupler=gf.components.grating_coupler_te,
        decorator=add_label_yaml_cutback_loopback4,
    )
    print(len(c.labels[0].text))
    print(c.labels[0].text)
    d = yaml.safe_load(c.labels[0].text) if yaml else json.loads(c.labels[0].text)
    c.show(show_ports=False)
