def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return

    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)


def reverse_stack(stack):
    if not stack:
        return

    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)


stack = list(map(int, input("Enter stack elements (bottom to top): ").split()))
reverse_stack(stack)

print(stack)