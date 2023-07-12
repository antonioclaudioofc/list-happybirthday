import { FastifyInstance } from "fastify";
import { z } from "zod";
import { prisma } from "../lib/prisma";

export async function birthdayRoutes(app: FastifyInstance) {
  app.get("/birthdays", async () => {
    const birthdays = await prisma.birthday.findMany({
      orderBy: {
        personName: "asc",
      },
    });

    return birthdays;
  });

  app.get("/birthdays/:id", async (request) => {
    // const { id } = request.params;

    const paramsSchema = z.object({
      id: z.string().uuid(),
    });

    const { id } = paramsSchema.parse(request.params);

    const birthday = await prisma.birthday.findUniqueOrThrow({
      where: {
        id,
      },
    });

    return birthday;
  });

  app.post("/birthdays", async (request) => {
    const bodySchema = z.object({
      personName: z.string(),
      dateOfBirth: z.string(),
      avatarBirthday: z.string(),
    });

    const { personName, dateOfBirth, avatarBirthday } = bodySchema.parse(
      request.body
    );

    const birthday = await prisma.birthday.create({
      data: {
        avatarBirthday,
        personName,
        dateOfBirth,
        userId: "0c0cb3f5-9ce6-45c8-b3ac-3c12e0dfd843",
      },
    });

    return birthday;
  });

  app.put("/birthdays/:id", async (request) => {
    const paramsSchema = z.object({
      id: z.string().uuid(),
    });

    const { id } = paramsSchema.parse(request.params);

    const bodySchema = z.object({
      personName: z.string(),
      dateOfBirth: z.string(),
      avatarBirthday: z.string(),
    });

    const { personName, dateOfBirth, avatarBirthday } = bodySchema.parse(
      request.body
    );

    const birthday = await prisma.birthday.update({
      where: {
        id,
      },
      data: {
        personName,
        dateOfBirth,
        avatarBirthday,
      },
    });

    return birthday
  });

  app.delete("/birthdays/:id", async (request) => {
    const paramsSchema = z.object({
      id: z.string().uuid(),
    });

    const { id } = paramsSchema.parse(request.params);

    const birthday = await prisma.birthday.delete({
      where: {
        id,
      },
    });
  });
}
