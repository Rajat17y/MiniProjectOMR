for i, var in enumerate(checkbox_vars):
        if var.get() == 1:  # If the checkbox is checked (state is 1)
            selected_options.append(checkbox_labels[i])
    label.config(text="Selected: " + ", ".join(selected_options))