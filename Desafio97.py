facebook = {"Ana", "Juan", "María", "Pedro", "Lucía"}
instagram = {"Juan", "María", "Lucía", "Carlos"}
twitter = {"María", "Lucía", "Carlos", "Sofía"}

# Usuarios que están en las tres redes
tres_redes = facebook & instagram & twitter

print("Usuarios que están en las tres redes:")
print(tres_redes)


# Usuarios que están solamente en una red
solo_facebook = facebook - instagram - twitter
solo_instagram = instagram - facebook - twitter
solo_twitter = twitter - facebook - instagram

solo_una = solo_facebook | solo_instagram | solo_twitter

print("\nUsuarios que están solamente en una red:")
print(solo_una)


# Usuarios que están en al menos dos redes
dos_o_mas = (
    (facebook & instagram)
    | (facebook & twitter)
    | (instagram & twitter)
)

print("\nUsuarios que están en al menos dos redes:")
print(dos_o_mas)