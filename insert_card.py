import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_card = '''                                                <div data-w-id="a1b2c3d4-e5f6-4890-abcd-ef1234567891"
                                                    class="programs-item-box item-four">
                                                    <div class="programs-list-wrap w-dyn-list">
                                                        <div role="list" class="programs-list w-dyn-items">
                                                            <div role="listitem" class="programs-item w-dyn-item">
                                                                <div class="programs-item-inner">
                                                                    <div class="programs-thumbnail"><img loading="lazy"
                                                                            src="https://cdn.prod.website-files.com/691eefbafb5f1e6cbbc807b3/693ffa866174ef7346c72921_programs-main-5.avif"
                                                                            alt="programs image"
                                                                            class="programs-image" /></div>
                                                                    <div class="program-item-overlays"></div>
                                                                    <div class="programs-item-flex">
                                                                        <div class="programs-info">
                                                                            <div class="programs-info-flex">
                                                                                <div class="programs-title-box">
                                                                                    <div class="programs-title">
                                                                                        WELLNESS / MINDFULNESS</div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class="programs-content">
                                                                            <div class="programs-content-flex">
                                                                                <div data-w-id="e3dfbe81-fc20-b426-b232-9cc0df08d912"
                                                                                    class="programs-icon-box">
                                                                                    <div class="programs-extra-info">
                                                                                        <div
                                                                                            class="programs-extra-info-inner">
                                                                                            <div
                                                                                                class="programs-extra-overlays">
                                                                                            </div>
                                                                                            <div
                                                                                                class="programs-extra-info-flex">
                                                                                                <div
                                                                                                    class="programs-extra-main">
                                                                                                    <div
                                                                                                        class="programs-extra-main-grid">
                                                                                                        <div
                                                                                                            class="programs-extra-main-info">
                                                                                                            <div
                                                                                                                class="programs-extra-main-title-box">
                                                                                                                <div
                                                                                                                    class="programs-extra-main-title">
                                                                                                                    Live
                                                                                                                    in
                                                                                                                    rhythm
                                                                                                                </div>
                                                                                                            </div>
                                                                                                            <div
                                                                                                                class="programs-extra-main-tag-box">
                                                                                                                <div
                                                                                                                    class="programs-extra-main-tag">
                                                                                                                    Rest.
                                                                                                                    Breathe.
                                                                                                                    Restore.
                                                                                                                </div>
                                                                                                            </div>
                                                                                                        </div>
                                                                                                        <div
                                                                                                            class="programs-extra-thumbnail">
                                                                                                            <img loading="lazy"
                                                                                                                src="https://cdn.prod.website-files.com/691eefbafb5f1e6cbbc807b3/69201071c5227a0865fe8805_programs-5.avif"
                                                                                                                alt="programs image"
                                                                                                                class="programs-extra-image" />
                                                                                                        </div>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div
                                                                                                    class="programs-extra-desc-box">
                                                                                                    <p
                                                                                                        class="programs-extra-desc">
                                                                                                        Stillness
                                                                                                        is
                                                                                                        a
                                                                                                        skill.

                                                                                                        ZAS
                                                                                                        guides
                                                                                                        you
                                                                                                        through
                                                                                                        breathwork,
                                                                                                        mindful
                                                                                                        movement,
                                                                                                        and
                                                                                                        deep
                                                                                                        restoration
                                                                                                        so
                                                                                                        you
                                                                                                        can
                                                                                                        feel
                                                                                                        whole
                                                                                                        again.
                                                                                                    </p>
                                                                                                </div>
                                                                                                <div
                                                                                                    class="programs-extra-features-box">
                                                                                                    <div
                                                                                                        class="programs-2-features-list">
                                                                                                        <div
                                                                                                            class="programs-2-features-item">
                                                                                                            <div
                                                                                                                class="programs-2-features-item-flex">
                                                                                                                <div
                                                                                                                    class="programs-2-features-label">
                                                                                                                    Mind
                                                                                                                </div>
                                                                                                                <div
                                                                                                                    class="programs-2-features-text">
                                                                                                                    Calm
                                                                                                                    &amp;
                                                                                                                    clarity
                                                                                                                </div>
                                                                                                            </div>
                                                                                                        </div>
                                                                                                        <div
                                                                                                            class="programs-2-features-item">
                                                                                                            <div
                                                                                                                class="programs-2-features-item-flex">
                                                                                                                <div
                                                                                                                    class="programs-2-features-label">
                                                                                                                    Body
                                                                                                                </div>
                                                                                                                <div
                                                                                                                    class="programs-2-features-text">
                                                                                                                    Rest
                                                                                                                    &amp;
                                                                                                                    restore
                                                                                                                </div>
                                                                                                            </div>
                                                                                                        </div>
                                                                                                        <div
                                                                                                            class="programs-2-features-item last">
                                                                                                            <div
                                                                                                                class="programs-2-features-item-flex">
                                                                                                                <div
                                                                                                                    class="programs-2-features-label">
                                                                                                                    Breath
                                                                                                                </div>
                                                                                                                <div
                                                                                                                    class="programs-2-features-text">
                                                                                                                    Deep
                                                                                                                    presence
                                                                                                                </div>
                                                                                                            </div>
                                                                                                        </div>
                                                                                                    </div>
                                                                                                </div>
                                                                                                <div
                                                                                                    class="programs-extra-desc-box">
                                                                                                    <p
                                                                                                        class="programs-extra-desc">
                                                                                                        Sometimes,
                                                                                                        slowing
                                                                                                        down
                                                                                                        is
                                                                                                        the
                                                                                                        most
                                                                                                        powerful
                                                                                                        move.
                                                                                                    </p>
                                                                                                </div>
                                                                                                <div
                                                                                                    class="programs-extra-button-box">
                                                                                                    <a data-w-id="0954ebad-a7f3-defe-36f2-e748ee80b251"
                                                                                                        href="#"
                                                                                                        class="button primary-button w-inline-block">
                                                                                                        <div
                                                                                                            class="button-wrap primary">
                                                                                                            <div
                                                                                                                class="button-flex">
                                                                                                                <div
                                                                                                                    class="button-text-box">
                                                                                                                    <div
                                                                                                                        class="button-text text-one">
                                                                                                                        Find
                                                                                                                        your
                                                                                                                        calm
                                                                                                                    </div>
                                                                                                                    <div
                                                                                                                        class="button-text text-two">
                                                                                                                        Find
                                                                                                                        your
                                                                                                                        calm
                                                                                                                    </div>
                                                                                                                </div>
                                                                                                                <div
                                                                                                                    class="button-icon-box">
                                                                                                                    <img src="https://cdn.prod.website-files.com/691ea5c2d38e36d02b948f36/693120f6a24d8ef7aeb4e03b_button-icon-2.svg"
                                                                                                                        loading="lazy"
                                                                                                                        alt="icon"
                                                                                                                        class="button-icon" />
                                                                                                                </div>
                                                                                                            </div>
                                                                                                        </div>
                                                                                                    </a>
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                    </div>
                                                                                    <div class="links-round">
                                                                                        <div class="links-background">
                                                                                        </div><img loading="lazy"
                                                                                            src="https://cdn.prod.website-files.com/691ea5c2d38e36d02b948f36/6932c8c50d6e2cfcfc8f46e6_plus-sign-button-round-2.svg"
                                                                                            alt="icon"
                                                                                            class="links-round-icon dark" /><img
                                                                                            loading="lazy"
                                                                                            src="https://cdn.prod.website-files.com/691ea5c2d38e36d02b948f36/696dd9d30b4c19ce09a5f653_plus-sign-button-round-3.svg"
                                                                                            alt="icon"
                                                                                            class="links-round-icon light" />
                                                                                    </div>
                                                                                </div>
                                                                                <div class="programs-desc-box">
                                                                                    <p class="programs-desc">ZAS guides
                                                                                        you through breathwork, mindful
                                                                                        movement, and deep restoration.
                                                                                    </p>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
'''

# The unique marker: programs-links div only appears once
marker = '<div class="programs-links">'
pos = content.find(marker)
if pos == -1:
    print("ERROR: marker not found")
else:
    # Insert new_card right before the programs-links div
    new_content = content[:pos] + new_card + content[pos:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"SUCCESS: Inserted item-four card at position {pos}")
    print(f"New file length: {len(new_content)} chars")
