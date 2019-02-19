import pytest
import os

from test.support.configure_test import app
from project.config import TestingConfig, DevelopmentConfig, ProductionConfig, env


@pytest.mark.skipif(
    env.bool("TRAVIS", default=False) == True, reason="Skipping this test on Travis CI."
)
def test_development_config(app):
    app = app(DevelopmentConfig)
    assert app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == env.str(
        "DEV_SQLALCHEMY_DATABASE_URI"
    )


def test_testing_config(app):
    app = app(TestingConfig)
    assert app.config["DEBUG"]
    assert app.config["TESTING"]
    assert not app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == env.str(
        "TESTING_SQLALCHEMY_DATABASE_URI"
    )


def test_production_config(app):
    app = app(ProductionConfig)
    assert not app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == env.str(
        "PROD_SQLALCHEMY_DATABASE_URI"
    )
