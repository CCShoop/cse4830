void explode_bomb(int level);
void complete_phase(int level);

int main(void) {
    char input[255];
    printf("Phase 5 >>> ");
    scanf("%s", &input);
    for (int i = 0; i < 18; i++) {
        eax = i;
        //cdqe
        eax = rbp+rax*1-0x20;
        edx = al;
        eax = i;
        //cdqe
        rcx (lea) rax*4+0x0;
        rax (lea) rip+0x2b8e;
        eax = rcx+rax*1;
        if (eax != edx)
            explode_bomb();
    }
    complete_phase();
}

void explode_bomb(int level) {
    printf("%d failed", level);
}

void complete_phase(int level) {
    printf("%d passed", level);
}
