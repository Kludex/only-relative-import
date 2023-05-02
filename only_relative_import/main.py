from libcst import ImportFrom
import libcst.matchers as m
import libcst as cst
from libcst.codemod import VisitorBasedCodemodCommand
from libcst.codemod import CodemodContext


class OnlyRelativeImportCommand(VisitorBasedCodemodCommand):  # type: ignore[misc]
    def __init__(self, context: CodemodContext, package_name: str) -> None:
        super().__init__(context)
        self.package_name = package_name

    def leave_ImportFrom(
        self, original_node: ImportFrom, updated_node: ImportFrom
    ) -> ImportFrom:
        if (
            updated_node.module is None
            or updated_node.relative
            or (
                not m.matches(
                    updated_node.module,
                    m.Name(self.package_name)
                    | m.Attribute(value=m.Name(self.package_name)),
                )
            )
        ):
            return updated_node

        raise RuntimeError("Found an absolute import!")


if __name__ == "__main__":
    import textwrap

    source = textwrap.dedent(
        """
    from . import foo
    from ..potato import foo
    # from potato import foo
    # from potato.foo import bar
    """
    )

    mod = cst.parse_module(source)
    mod = mod.visit(OnlyRelativeImportCommand(CodemodContext(), "potato"))
    print(mod.code)
