import typer


def calculate_yield(
    average_stems_per_meter: float,
    average_grains_in_basket: float,
    average_weight_thousand_grains: float,
):
    typer.echo(
        round(
            (
                average_stems_per_meter
                * average_grains_in_basket
                * average_weight_thousand_grains
            )
            / 1e5,  # 1000 (grains) * 10 (meters -> hectares).
        ),
    )


if __name__ == "__main__":
    typer.run(calculate_yield)
