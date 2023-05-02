import pytest
from libcst.codemod import CodemodTest
from only_relative_import.main import OnlyRelativeImportCommand


class TestOnlyRelativeImportCommand(CodemodTest):  # type: ignore[misc]
    TRANSFORM = OnlyRelativeImportCommand

    def test_simple(self) -> None:
        source = """
            from potato import foo
        """
        with pytest.raises(RuntimeError):
            self.assertCodemod(source, source, package_name="potato")

    def test_other_imports(self) -> None:
        source = """
            from other import foo

            from ..potato import foo
        """
        self.assertCodemod(source, source, package_name="potato")

    def test_only_relative(self) -> None:
        source = """
            from . import foo
            from ..potato import foo
            from ...potato import foo
        """
        self.assertCodemod(source, source, package_name="potato")
