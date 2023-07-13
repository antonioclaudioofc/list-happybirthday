import { FastifyInstance } from "fastify";
import { z } from "zod";
import { prisma } from "../lib/prisma";
import bcrypt from "bcryptjs";

export async function authRoutes(app: FastifyInstance) {
  app.post("/register", async (request) => {
    const bodySchema = z.object({
      name: z.string(),
      username: z.string(),
      email: z.string(),
      password: z.string(),
      avatarUser: z.string(),
    });

    const { name, username, email, avatarUser, password } = bodySchema.parse(
      request.body
    );

    const hashedPassword = await bcrypt.hash(password, 10);

    const auth = await prisma.user.create({
      data: {
        name,
        username,
        email,
        avatarUser,
        password: hashedPassword,
      },
    });

    return auth;
  });
}
