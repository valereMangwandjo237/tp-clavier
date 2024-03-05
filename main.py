import pygame
import sys

pygame.init()

largeur, hauteur = 600, 450
fenetre = pygame.display.set_mode((largeur, hauteur))
fenetre.fill((255, 255, 255))  # Fond blanc
pygame.display.set_caption("Détection des touches du clavier")

font = pygame.font.Font(None, 36)

def afficher_message_bienvenue():
    message = "Appuyer sur une touche du clavier"
    texte = font.render(message, True, (0, 0, 0))  # Texte noir
    rect = texte.get_rect(center=(largeur // 2, hauteur // 2))
    fenetre.blit(texte, rect)
    pygame.display.flip()

def afficher_touche_presse(touche):
    fenetre.fill((255, 255, 255)) 
    texte = font.render(f"Touche pressee: {touche}", True, (0, 0, 0))  # Texte noir
    rect = texte.get_rect(center=(largeur // 2, hauteur // 2)) #creer un zone au centre
    fenetre.blit(texte, rect) #appliquer le texte au centre
    pygame.display.flip() #appliquer les modifictions

def main():
    afficher_message_bienvenue()

    touche_presse = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                touche_presse = event.unicode

        if touche_presse is not None:
            afficher_touche_presse(touche_presse)
            touche_presse = None

if __name__ == "__main__":
    main()
