
# FCSC 2023: Comparaison
## Stillwolfing

Here is the context:

![context](/assets/img/CTFs/FCSC2023/Intro/comparaison/context.png)


We are given:
- the code of the machine (machine.py)
- a code to translate the assembly code into hex format in order to send it to the server (assembly.py)
- the code present on the server (challenge.py)


The harder was to understand the syntax of the asm code they created.

Here is the python code I created:

```python
from assembly import assembly

# create the assembly code
code = """
CMP R5, R6
JNZA different
MOV R0, #0x0
JA end


different:
    MOV R0, #0x1

end:
    MOV R0, R0  // instruction inutile pour éviter un "warning"

STP
"""

# create the assembly object
asm = assembly(code.split("\n"))

print(asm)
```

R5 and R6 contains the 2 values that we have to compare.

We compare the two values.
If they are equal, we set the value of R0 to 0 and jump to the end.

If they are different, we jump to the label "different" and set the value  of R0 to 1.

Let's look at the output:

![output](/assets/img/CTFs/FCSC2023/Intro/comparaison/output.png)

It seems that our code has been translated to hex without problem.

Let's send it to the server:

![flag](/assets/img/CTFs/FCSC2023/Intro/comparaison/flag.png)

One more flag 🙂!



