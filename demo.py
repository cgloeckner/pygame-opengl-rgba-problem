#!/bin/python3

import pygame
import OpenGL.GL as gl

def loadTexture(fname):
    surface = pygame.image.load('demo.png').convert_alpha()
    data = pygame.image.tostring(surface, "RGBA", 1)
    w = surface.get_width()
    h = surface.get_height()

    gl.glEnable(gl.GL_TEXTURE_2D)
    texid = gl.glGenTextures(1)
    gl.glBindTexture(gl.GL_TEXTURE_2D, texid)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, w, h, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, data)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
    gl.glTexParameterf(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)

    return texid


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT)
    gl.glClearColor(0.0, 0.0, 1.0, 0.0)
    running = True

    tex = loadTexture("demo.png")
    
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glOrtho(0.0, 640, 480, 0.0, -0.01, 10.0)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        gl.glBegin(gl.GL_QUADS)
        # topleft
        gl.glTexCoord2f(0.0, 0.0)
        gl.glVertex3f(0.0, 0.0, 0.0)
        # topright
        gl.glTexCoord2f(1.0, 0.0)
        gl.glVertex3f(100.0, 0.0, 0.0)
        # bottomright
        gl.glTexCoord2f(1.0, 1.0)
        gl.glVertex3f(100.0, 100.0, 0.0)
        # bottomleft
        gl.glTexCoord2f(0.0, 1.0)
        gl.glVertex3f(0.0, 100.0, 0.0)
        gl.glEnd()
        
        pygame.display.flip()


if __name__ == '__main__':
    main()
